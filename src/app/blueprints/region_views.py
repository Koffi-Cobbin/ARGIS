__author__ = "Cobbin"

from flask import Blueprint, request,url_for, flash, render_template
from src.app.models.regions.region import Region 
import src.app.models.regions.errors as RegionErrors 

region_blueprint = Blueprint('regions', __name__)


@region_blueprint.route('/regions', methods=['GET'])
def regions():
    regions = Region.query.all()
    region_dict, *_ = regions
    keys = list(region_dict.keys())
    cnt = len(keys)
    return render_template('base.html', collection=regions, keys=keys, cnt=cnt)

@region_blueprint.route('/update_region', methods=['POST'])
def update_region():
    pass 
