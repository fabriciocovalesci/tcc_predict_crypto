from flask import Blueprint, render_template
from flask import jsonify
import re
import locale

locale.setlocale(locale.LC_ALL, '')

from models_predict import PricePredictor
from app.utils.helpers import Helper



helper_crypto = Helper()

predict = Blueprint("predict", __name__)


@predict.route("/coin/<crypto_name>", methods=['GET'])
def access_coin(crypto_name):
    try:
        if re.search(r"\s", crypto_name):
            crypto_name = crypto_name.replace(" ", "_")
        symbol = helper_crypto.get_symbol_by_name(crypto_name)
        model = PricePredictor(symbol)
        prediction = model.predict_price()
        return render_template("coin.html", crypto_name=crypto_name, symbol=symbol, prediction=prediction)
    except Exception as err:
        print(f"ERROR: {err}")

