#!/bin/bash
python -m pip install virtualenv
python -m virtualenv virtual
source virtual/bin/activate
pip install flask
pip install requests
python main.py
