#!/bin/bash

echo "Running build script..."

source /home/sandih/env/bin/activate

export FLASK_APP=app.py
export FLASK_ENV=development

flask run