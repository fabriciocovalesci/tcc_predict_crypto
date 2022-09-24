import httpx
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64
import locale
from flask import send_file
import pandas as pd
import os
from app.config import DF_CORR, IMG_PLOT
from app.utils.helpers import * 

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

BASE_URL_COIN = "https://api.coingecko.com/api/v3/"


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

def get_symbol_by_name(crypto):
    data = [
        { "name": "Bitcoin", "symbol": "btc" },
        { "name": "Ethereum", "symbol": "eth" },
        { "name": "Binance Coin", "symbol": "bnb" },
        { "name": "Ripple", "symbol": "xrp" },
        { "name": "Cardano", "symbol": "ada" },
        { "name": "Solana", "symbol": "sol" },
        { "name": "Dogecoin", "symbol": "doge" },
        { "name": "Polkadot", "symbol": "dot" },
        { "name": "Polygon", "symbol": "matic" },
        { "name": "Dai", "symbol": "dai" },
            ]
    symbol = [item.get("symbol") for item in data if item.get("name") == crypto ][0]
    return symbol


def request_coingecko(crypto):
    try:
        endpoint = f"simple/price?ids={crypto}&vs_currencies=usd"
        resp = httpx.get(f"{BASE_URL_COIN}{endpoint}")
        if resp.status_code == 200:
            return resp.json()
    except Exception as err:
        print(f"ERROR ", err)


def get_price_coin(crypto, body):
    id = [item.get("id") for item in content_cards if item.get("crypto_name") == crypto][0]
    if body:
        return request_coingecko(id)
    else:
        response = request_coingecko(id)
        if response and isinstance(response.get(id, None), dict) and isinstance(response.get(id).get("usd", None), float):
            return  locale.currency(response.get(id).get("usd"), grouping=True, symbol=True, international=True)
        return f"nada-{crypto}"
        
     
def create_image_corr():
    my_corr = pd.read_csv(DF_CORR, delimiter=',')
    fig,ax=plt.subplots(figsize=(16,8))
    ax=sns.heatmap(my_corr.corr(),
            vmin = -1, vmax = 1, annot = True, cmap = 'BrBG')
    img = io.BytesIO()
    fig.savefig(img)
    name_image = f"fig.png"
    plt.savefig(f"{IMG_PLOT}/{name_image}", format='png')
    plt.close()
    img.seek(0)
    # plot_url = base64.b64encode(img.getvalue())
    return name_image
