#!/bin/bash
pip install virtualenv
python3 -m virtualenv virtual
source virtual/bin/activate
pip install flask
pip install requests
python main.py
deactivate