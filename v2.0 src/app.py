__author__ = "Koffi-Cobbin"
from flask import render_template, request
from common.database import Database #src.
from config import app

from models.users.views import user_blueprint #src.
from models.regions.views import region_blueprint #src.
from models.towns.views import town_blueprint #src.
from models.polylines.views import line_blueprint
app.register_blueprint(user_blueprint, url_prefix="/users")
app.register_blueprint(region_blueprint, url_prefix="/regions")
app.register_blueprint(town_blueprint, url_prefix="/towns")
app.register_blueprint(line_blueprint, url_prefix="/lines")
    
#res = Database.insert("polyline", ["2","[(4,5),(5,6),(6,7)]", "1"])       

    
    
    