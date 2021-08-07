__author__ = "Cobbin"
from flask import Flask
from flask_mysqldb import MySQL 

app = Flask(__name__)
app.secret_key = app.secret_key = os.environ.get("SECRETE_KEY")
app.config['MYSQL_HOST'] = os.environ.get("MYSQL_HOST") 
app.config['MYSQL_USER'] = os.environ.get("MYSQL_USER")
app.config['MYSQL_PASSWORD'] = os.environ.get("MYSQL_PASSWORD")
app.config['MYSQL_DB'] = os.environ.get("MYSQL_DB")
mysql = MySQL(app)
