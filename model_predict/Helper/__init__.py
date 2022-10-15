import pandas as pd
import yfinance as yf
from datetime import datetime


class Helper:
    
    def __init__(self, date_init=None):
        self._pairs = [
                { "name": "Bitcoin", "pair": "BTC" },
                { "name": "Ethereum", "pair": "ETH" },
                { "name": "Cardano", "pair": "ADA" },
                { "name": "Dogecoin", "pair": "DOGE" },
                { "name": "Ripple", "pair": "XRP" },
                { "name": "Dai", "pair": "DAI" },
                { "name": "Plkadot", "pair": "DOT" },
                { "name": "Polygon", "pair": "MATIC" },
                { "name": "Solana", "pair": "SOL" },
                { "name": "Binancecoin", "pair": "BNB" }
            ]
        self.date_init = "2014-01-01" | date_init
        self.date_now = datetime.strftime(datetime.now(), "%Y-%m-%d")
        
        
    @property
    def pairs(self):
        return self._pairs
    
    
    def validate_cryptocurrency(self, crypto):
        if isinstance(crypto, str) and len([pair for pair in self.pairs if crypto.upper() in pair.get('pair')]) != 0:
            return crypto
        return None
    
    
    def download(self, crypto):
        try:
            return yf.download(f"{crypto}-USD", self.date_init, self.date_now)
        except Exception as err:
            print(f"ERRROR {err}")
        
    
    def download_one_crypto(self, crypto):
        try:
            if self.validate_cryptocurrency(crypto):
                return self.download(crypto.upper())
        except Exception as err:
            print(f"ERRROR {err}")
            
    
    def download_all_crypto_dataframe(self):
        results = []
        for crypto in self.pairs:
            result = self.download_one_crypto(crypto.get('pair'))
            results.append(pd.DataFrame(result.Close).rename(columns = {'Close': crypto.get('name')}))
        return results   
        
