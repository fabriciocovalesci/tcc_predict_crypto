from flask import Blueprint, render_template
from flask import jsonify, request

from models_predict import load_model_bitcoin

home = Blueprint("home", __name__)


@home.route('/')
def index():
    return render_template("base.html")


@home.route("/predict", methods=['POST'])
def predict():
    horizon = int(request.json['horizon'])
    model = load_model_bitcoin()
    future2 = model.make_future_dataframe(periods=horizon)
    forecast2 = model.predict(future2)
    data = forecast2[['ds', 'yhat', 'yhat_lower', 'yhat_upper']][-horizon:]
    ret = data.to_json(orient='records', date_format='iso')
    return ret
