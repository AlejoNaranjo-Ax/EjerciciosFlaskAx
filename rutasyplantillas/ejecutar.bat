@echo off
py -m pip install -r requirements.txt
start "" http://127.0.0.1:3600
py App.py
pause
