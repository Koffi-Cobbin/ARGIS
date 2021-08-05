__author__ = "Cobbin"

from flask import Blueprint, request,url_for, flash, render_template
from models.polylines.polyline import Polyline #src.
import models.polylines.errors as LineErrors #src.
from common.database import Database

line_blueprint = Blueprint('lines', __name__)


@line_blueprint.route('/lines', methods=['GET'])
def lines():
    polylines = Database.select_from_where("*", "polyline")
    line_dict, *_ = polylines
    keys = list(line_dict.keys())
    cnt = len(keys)
    return render_template('base.html', collection=polylines, keys=keys, cnt=cnt)