#!/usr/bin/bash

virtualenv env
pip install -r requirements.txt
. env/bin/activate
python main.py