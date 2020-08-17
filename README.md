 REST API CARS


Application URL https://car-rest-api.herokuapp.com/

Prerequisites
To start you have to have installed Python 3.8

Getting Started
To start the project locally

Clone repository

$ git clone https://github.com/Ogorodnyk/Rest_Api_Cars.git
I recommend using virtualenv

$ virtualenv venv

for unix users:
$ source venv/bin/activate 

for windows users:
$ source venv/Scripts/activate
then

next step is to install all required packages

$ pip install -r requirements.txt
before running app, make all needed migrations

$ python manage.py migrate
now you can start

$ python manage.py runserver
open a browser and go to

http://127.0.0.1:8000
