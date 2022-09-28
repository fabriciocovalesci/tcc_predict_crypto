from flask import Blueprint, render_template
from flask import jsonify, request
import os
from app.utils.helpers import Helper

home = Blueprint("home", __name__)


helper_crypto = Helper("2020-01-01")


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
    new_card = []
    
    print("helper_crypto ", helper_crypto.pairs)
    # for item in content_cards:
    #     resp = get_price_coin(item.get('crypto_name'), False)
    #     new_card.append({
    #     "crypto_name": item.get('crypto_name'), "par": item.get('par'), "trend": item.get('trend'), "image": item.get('image'), "price": resp
    #     })
    return render_template("home.html", content_cards=content_cards, plot_url='corr.png')


        
@home.route("/corr", methods=['GET'])
def corr():
    return helper_crypto.main()