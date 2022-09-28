import httpx
import locale
import re
from app.config import DF_CORR, IMG_PLOT
from app.utils.helpers import Helper

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

BASE_URL_COIN = "https://api.coingecko.com/api/v3/"


helper_crypto = Helper()


class client:
    
    def __init__(self):
        pass



def request_coingecko(crypto):
    try:
        endpoint = f"simple/price?ids={crypto}&vs_currencies=usd"
        resp = httpx.get(f"{BASE_URL_COIN}{endpoint}")
        if resp.status_code == 200:
            return resp.json()
    except Exception as err:
        print(f"ERROR ", err)



def get_price_coin(crypto, body):
    if re.search(r"\s", crypto):
        crypto = crypto.replace(" ", "_")
    id = [item.get("id") for item in helper_crypto.pairs if item.get("name").lower() == crypto.lower()][0]
    print("id ", id)
    if body:
        return request_coingecko(id)
    else:
        response = request_coingecko(id)
        if response and isinstance(response.get(id, None), dict) and isinstance(response.get(id).get("usd", None), float):
            return  locale.currency(response.get(id).get("usd"), grouping=True, symbol=True, international=True)
        return f"nada-{crypto}"