from flask import Blueprint, render_template
from flask import jsonify, request
import os

home = Blueprint("home", __name__)


@home.route('/')
def index():
    content_cards = [
        {"crypto_name": "Bitcoin", "par": "BTC-USD", "trend": "Alta", "image": "bitcoin.png"},
        {"crypto_name": "Ethereum", "par": "ETH-USD", "trend": "Alta", "image": "ethereum.png"},
        {"crypto_name": "Binance Coin", "par": "BNB-USD", "trend": "Alta", "image": "binancecoin.png"},
        {"crypto_name": "Ripple", "par": "XRP-USD", "trend": "Alta", "image": "ripple.png"},
        {"crypto_name": "Cardano", "par": "ADA-USD", "trend": "Alta", "image": "cardano.png"},
        {"crypto_name": "Solana", "par": "SOL-USD", "trend": "Alta", "image": "solana.png"},
        {"crypto_name": "Dogecoin", "par": "DOGE-USD", "trend": "Alta", "image": "dogecoin.png"},
        {"crypto_name": "Polkadot", "par": "DOT-USD", "trend": "Alta", "image": "polkadot.png"},
        {"crypto_name": "Polygon", "par": "MATIC-USD", "trend": "Alta", "image": "polygon.png"},
        {"crypto_name": "Dai", "par": "DAI-USD", "trend": "Alta", "image": "dai.png"}
    ]
    return render_template("home.html", content_cards=content_cards)
