import httpx

BASE_URL_COIN = "https://api.coingecko.com/api/v3/"


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




def get_price_coin(crypto):
    crypto = crypto.lower()
    endpoint = f"simple/price?ids={crypto}&vs_currencies=usd"
    resp = httpx.get(f"{BASE_URL_COIN}{endpoint}")
    if resp.status_code == 200:
        return resp.json()