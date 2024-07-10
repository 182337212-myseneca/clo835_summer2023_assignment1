from flask import Flask, render_template, request
from pymysql import connections
import os
import random
import argparse
from urllib.parse import quote as url_quote

app = Flask(__name__)

# Set environment variables
os.environ["DBHOST"] = "localhost"
os.environ["DBUSER"] = "root"
os.environ["DBPWD"] = "password"
os.environ["DATABASE"] = "employees"
os.environ["DBPORT"] = "3306"
os.environ["APP_COLOR"] = "lime"

DBHOST = os.environ.get("DBHOST")
DBUSER = os.environ.get("DBUSER")
DBPWD = os.environ.get("DBPWD")
DATABASE = os.environ.get("DATABASE")
COLOR_FROM_ENV = os.environ.get('APP_COLOR')
DBPORT = int(os.environ.get("DBPORT"))

# Create a connection to the MySQL database
try:
    db_conn = connections.Connection(
        host=DBHOST,
        port=DBPORT,
        user=DBUSER,
        password=DBPWD, 
        db=DATABASE
    )
except pymysql.err.OperationalError as e:
    print(f"Error connecting to MySQL: {e}")
    exit(1)

output = {}
table = 'employee';

# Define the supported color codes
color_codes = {
    "red": "#e74c3c",
    "green": "#16a085",
    "blue": "#89CFF0",
    "blue2": "#30336b",
    "pink": "#f4c2c2",
    "darkblue": "#130f40",
    "lime": "#C1FF9C",
}

# Create a string of supported colors
SUPPORTED_COLORS = ",".join(color_codes.keys())

# Generate a random color
COLOR = random.choice(["red", "green", "blue", "blue2", "darkblue", "pink", "lime"])

#... rest of the code remains the same...
