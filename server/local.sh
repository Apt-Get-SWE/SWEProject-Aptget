#!/bin/bash

# run our server locally:
PYTHONPATH=$(pwd):$PYTHONPATH
FLASK_APP=src/endpoints/endpoints.py
flask run --host=0.0.0.0 --port=8000
