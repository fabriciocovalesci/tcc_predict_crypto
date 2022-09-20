from flask import Blueprint, render_template
from flask import jsonify, request
import json
import datetime
import os

from models_predict import PricePredictor
from app.utils.helpers import get_symbol_by_name, get_price_coin


predict = Blueprint("predict", __name__)


@predict.route("/coin/<crypto_name>", methods=['GET'])
def access_coin(crypto_name):
    symbol = get_symbol_by_name(crypto_name)
    print("crypto_name ", crypto_name)
    price_current = get_price_coin(crypto_name)
    return render_template("coin.html", crypto_name=crypto_name, symbol=symbol, price_current=price_current.get(crypto_name.lower()).get("usd"))


@predict.route("/predict", methods=['POST'])
def predict_coin():
    try:
        period = int(request.json['period'])
        crypto = request.json['crypto']
        symbol = get_symbol_by_name(crypto)
        today = datetime.datetime.strftime(datetime.datetime.today(), "%Y-%m-%d")
        model = PricePredictor(today, period, symbol)
        prediction = model.predict()   
        return jsonify(prediction)
    except Exception as e:
        print("error", e)