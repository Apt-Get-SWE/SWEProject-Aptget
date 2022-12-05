#!/bin/bash

# run our server locally:
cd ..
gunicorn server.app:app
