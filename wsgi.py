#!/usr/bin/python3
import sys 

sys.path.insert(0, "/var/www/html/Dash/")
from app import app
application = app.server