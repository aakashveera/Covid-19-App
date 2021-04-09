# COVID-19 CLASSIFICATION APP

This repo consists of Covid-19 Classification Web App which classifies Covid +ve/-ve with Chest X-ray Image created using Python Flask and Deep learning(Pytorch Library).

Covid-19 labelled chest x-ray images have been collected from multiple sources. Efficientnet-B3 is used for modelling and is build with pytorch. It is then made as a simple web-app using Flask.

The Web App is dockerized and the public image name is aakashveera/covid-19. The same is deployed onto Google Cloud with Kubernetes. 

### To use the Web App,
1. If you have docker all you need is two commands <b><i>docker pull aakashveera/covid-19</i></b> and <b><i>docker run -p 5000:5000 aakashveera/covid-19</i></b>
2. If you don't have docker,
    1. The app requires torch, Flask, opencv-python, torchvision, efficientnet-pytorch, numpy libraries. Install everything using pip command (pip install libraray-name).
    2. Download the repo and simply navigate to the repo using cmd and run <b><i>python server.py</b></i>. You can now can access the web app at localhost:5000 in your browser.
