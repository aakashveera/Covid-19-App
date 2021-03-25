from flask import Flask, request, render_template,url_for,redirect,session
import werkzeug


import os
import cv2
import torch
import numpy as np
import torchvision.transforms as transforms
from efficientnet_pytorch import EfficientNet
from torch.autograd import Variable

use_cuda = torch.cuda.is_available()
device = torch.device("cuda:0" if use_cuda else "cpu")

torch.manual_seed(42)

model = torch.load("model.pt",map_location='cpu')
model.to(device)
model.eval()

transform = transforms.Compose([
        transforms.ToPILImage(),
        transforms.Resize(224),       
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406],
                             [0.229, 0.224, 0.225])
    ])



app = Flask(__name__)
app.secret_key = "abc"  

@app.route('/')
def home():
	return render_template("index.html")

@app.route('/predict', methods = ['POST','GET'])
def file_upload():
	if request.method== 'POST':
		files_get = request.files['img']
		filename = werkzeug.utils.secure_filename(files_get.filename)
		files_get.save(filename)

		img = transform(cv2.imread(filename)).unsqueeze_(0)
		input = Variable(img)
		input = input.to(device)
		
		with torch.no_grad():
			label = model(input).data.numpy().argmax()

		print(label)

		if label==1:
			session['result'] = 'positive'
		else:
			session['result'] = 'negative'

		os.remove(filename)

		return redirect(url_for(".result"))

	if request.method== 'GET':
		return redirect(url_for(".home"))

@app.route('/result', methods = ['POST','GET'])
def result():
	try:
		result = session['result']
		session.clear()
		print(request.method)
		return render_template("result.html", data=[result])
	except:
		return redirect(url_for(".home"))

app.run(host ='0.0.0.0', port = 5000,debug=True)