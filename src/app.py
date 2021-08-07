__author__ = "Koffi-Cobbin"
from flask import render_template, request
from src.database.db import db 
from src.config import app

from src.app.models.users.views import user_blueprint 
from src.app.models.regions.views import region_blueprint 
from src.app.models.towns.views import town_blueprint 
from src.app.models.polylines.views import line_blueprint
app.register_blueprint(user_blueprint, url_prefix="/users")
app.register_blueprint(region_blueprint, url_prefix="/regions")
app.register_blueprint(town_blueprint, url_prefix="/towns")
app.register_blueprint(line_blueprint, url_prefix="/lines")
  
