__author__ = "Cobbin"

from flask import Blueprint, request,url_for, flash, render_template, redirect
from models.towns.town import Town #src.
import models.users.errors as UserErrors #src.
from common.database import Database

town_blueprint = Blueprint('towns', __name__)

@town_blueprint.route('/towns', methods=['GET', 'POST'])
def towns():
    if request.method == 'POST':
        town_name = request['name']
        region = request['region']
        regions = [{"Accra":"ACC01"}, {"Ashanti Region":"ASH02"}, {"Northern Region":"NTH03"}]
        for region in regions:
            if region in regions.keys():
                region_id = regions[region]
                print("Was here")
            else:
                return redirect(url_for('.towns'))
        town_id = region_id + "GH"
        res = Database.insert("town", [town_id, town_name, region_id])
        return redirect(url_for('.towns'))

    towns = Database.select_from_where("*", "town")
    town_dict, *_ = towns
    keys = list(town_dict.keys())
    return render_template('base.html', collection=towns, keys=keys)
    

@town_blueprint.route('/gettownlines/<string:town_id>', methods=['GET'])
def gettownlines(town_id):
    res = Database.select_from_where("name", "town", f"town_id='{town_id}'")
    town, *_ = res
    town_lines = Database.select_from_where("*", "town_line", f"town_id='{town_id}'")
    town_dict, *_ = town_lines
    keys = list(town_dict.keys())
    return render_template('town_lines.html', collection=town_lines, keys=keys, town=town)