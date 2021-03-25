docker build -t aakashveera/covid-19:latest -t aakashveera/covid-19:$GIT_SHA .

docker push aakashveera/covid-19:$GIT_SHA

docker push aakashveera/covid-19:latest

kubectl apply -f k8s

kubectl set image deployments/flask-app-deployment flask-app=aakashveera/covid-19:$GIT_SHA