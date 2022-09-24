from flask import Blueprint, render_template
from flask import jsonify, request
import os
from app.utils.helpers import create_image_corr, get_price_coin

home = Blueprint("home", __name__)


@home.route('/')
def index():
    content_cards = [
        {"crypto_name": "Bitcoin", "par": "BTC-USD", "trend": "Alta", "image": "bitcoin.png", "id": "bitcoin"},
        {"crypto_name": "Ethereum", "par": "ETH-USD", "trend": "Alta", "image": "ethereum.png", "id": "ethereum"},
        {"crypto_name": "Binance Coin", "par": "BNB-USD", "trend": "Alta", "image": "binancecoin.png", "id": "binancecoin"},
        {"crypto_name": "Ripple", "par": "XRP-USD", "trend": "Alta", "image": "ripple.png", "id": "ripple"},
        {"crypto_name": "Cardano", "par": "ADA-USD", "trend": "Alta", "image": "cardano.png", "id": "cardano"},
        {"crypto_name": "Solana", "par": "SOL-USD", "trend": "Alta", "image": "solana.png", "id": "solana"},
        {"crypto_name": "Dogecoin", "par": "DOGE-USD", "trend": "Alta", "image": "dogecoin.png", "id": "dogecoin"},
        {"crypto_name": "Polkadot", "par": "DOT-USD", "trend": "Alta", "image": "polkadot.png", "id": "polkadot"},
        {"crypto_name": "Polygon", "par": "MATIC-USD", "trend": "Alta", "image": "polygon.png", "id": "matic-network"},
        {"crypto_name": "Dai", "par": "DAI-USD", "trend": "Alta", "image": "dai.png", "id": "dai"}
    ]
    return render_template("home.html", content_cards=content_cards, plot_url='corr.png')


        
# @home.route("/visualize", methods=['GET'])
# def visualize():
#     return create_image_corr()
