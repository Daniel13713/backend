#!/usr/bin/env bash
#Activate viertual enviroment
source venv/bin/activate

#install requeriments
pip3 install -r requirements.txt

#Setting of development
export FLASK_APP=main.py
export FLASK_DEBUG=1
export FLASK_ENV=development

#run flask
#flask run
