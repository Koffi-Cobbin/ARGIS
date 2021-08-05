__author__ = "Cobbin"

from flask import Blueprint, request,url_for, flash, render_template
from models.regions.region import Region #src.
import models.regions.errors as RegionErrors #src.
from common.database import Database

region_blueprint = Blueprint('regions', __name__)


@region_blueprint.route('/regions', methods=['GET'])
def regions():
    regions = Database.select_from_where("*", "region")
    region_dict, *_ = regions
    keys = list(region_dict.keys())
    cnt = len(keys)
    return render_template('base.html', collection=regions, keys=keys, cnt=cnt)

@region_blueprint.route('/update_region', methods=['POST'])
def update_region():
    res = Database.update("region", f"polylines='{column_value}'", f"{codition}")
    cnt = len(keys)    