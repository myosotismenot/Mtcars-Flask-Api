# Mtcars-Flask-Api

STATS 418 HW 3 - Timothy Tu
This repo contains the files I used to create a simple linear regression using the numerical predictors of the well-known mtcars dataset to predict mpg. You should be able to reproduce the same results.

## Files
* `requirements.txt` - Python libraries utilized, to build docker image
* `docker-compose.yml` - file used to build docker image
* `Dockerfile` - file used to build docker image
* `prediction.py` - python file containing function for linear regression model
* `server.py` - python file for flask api to get predictions
* `mtcars.csv` - csv file containing the mtcars data

## Test this on your local machine by building with Docker

1. Clone this repo
2. Build the image with the dockerfiles. Make sure in terminal, you are in the folder containg the repo/files related to docker.
```
docker compose up -d
```
3. Make sure the localhost server is running.
```
curl http://localhost:5001/
```

If it is, you should get 
```
server is up - nice job!
```

4. Test this command
```
curl -X POST "http://localhost:5001/predict_price" -H "Content-Type:application/json" -d '{"cyl":6,"disp":160.0,"hp":110,"drat":3.90,"wt":2.620,"qsec":16.46,"gear":4,"carb":4}'
```

Expected response:
```
"predicted mpg": 22.024871346931384
```

## Test via Google Cloud
1. Visit this [flask link](https://mtcars-flask-api-1099088179937.us-central1.run.app/) to see if the server is running. If so, you can test via terminal

```
curl -X POST "https://mtcars-flask-api-1099088179937.us-central1.run.app/predict_price" -H "Content-Type:application/json" -d '{"cyl":6,"disp":160.0,"hp":110,"drat":3.90,"wt":2.620,"qsec":16.46,"gear":4,"carb":4}'
```
Expected Response:
```
"predicted mpg": 22.024871346931384
```
2. If the flask api is not up, you can create it your own by composing the image as done earlier and pushing it to your own docker hub repository to use via google cloud run.
