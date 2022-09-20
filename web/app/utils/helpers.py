

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