from flask import Blueprint, render_template
from flask import jsonify, request
import os
import json
from app.utils.helpers import Helper
from app.config import DATA_CORR

home = Blueprint("home", __name__)

helper_crypto = Helper()


@home.route('/', methods=['GET'])
def index():
    f = open(os.path.join(DATA_CORR, "corr.json"))
    data = json.load(f)
    f.close()
    return render_template("home.html", content_cards=helper_crypto.pairs, crypto_corr=data)


        
@home.route("/corr", methods=['GET'])
def corr():
    return helper_crypto.main()