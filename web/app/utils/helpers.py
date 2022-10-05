import httpx
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64
import locale
from flask import send_file
import pandas as pd
import yfinance as yf
from datetime import datetime
from functools import reduce
import os
from app.config import IMG_PLOT
from app.utils.helpers import * 

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')



class Helper:
    
    def __init__(self, date_init="2014-01-01"):
        self.pairs = [
                {"name": "Bitcoin", "pair": "BTC-USD", "trend": "Alta", "image": "bitcoin.png", "id": "bitcoin"},
                {"name": "Ethereum", "pair": "ETH-USD", "trend": "Alta", "image": "ethereum.png", "id": "ethereum"},
                {"name": "Binance_Coin", "pair": "BNB-USD", "trend": "Alta", "image": "binancecoin.png", "id": "binancecoin"},
                {"name": "Ripple", "pair": "XRP-USD", "trend": "Alta", "image": "ripple.png", "id": "ripple"},
                {"name": "Cardano", "pair": "ADA-USD", "trend": "Alta", "image": "cardano.png", "id": "cardano"},
                {"name": "Solana", "pair": "SOL-USD", "trend": "Alta", "image": "solana.png", "id": "solana"},
                {"name": "Dogecoin", "pair": "DOGE-USD", "trend": "Alta", "image": "dogecoin.png", "id": "dogecoin"},
                {"name": "Polkadot", "pair": "DOT-USD", "trend": "Alta", "image": "polkadot.png", "id": "polkadot"},
                {"name": "Polygon", "pair": "MATIC-USD", "trend": "Alta", "image": "polygon.png", "id": "matic-network"},
                {"name": "Dai", "pair": "DAI-USD", "trend": "Alta", "image": "dai.png", "id": "dai"}
            ]
        self.date_init = date_init
        self.date_now = datetime.strftime(datetime.now(), "%Y-%m-%d")
        
    
    def __repr__(self):
        return f"{self.__class__}"
    
    
    @property
    def pairs(self):
        return self._pairs
    
    
    @pairs.setter
    def pairs(self, value):
        if not isinstance(value, list):
            raise ValueError("Pares devem ser uma lista de objetos")
        self._pairs = value
        
        
    @property
    def date_init(self):
        return self._date_init
    
    
    @date_init.setter
    def date_init(self, value):
        if not isinstance(value, str):
            raise ValueError("Valor deve ser uma string de data: yyy-mm-dd")
        self._date_init = value
        
        
    def validate_cryptocurrency(self, crypto):
        if isinstance(crypto, str) and len([pair for pair in self.pairs if crypto.upper() in pair.get('pair')]) != 0:
            return crypto
        return None
    
    
    def get_symbol_by_name(self, crypto):
        symbol = [item.get("pair").lower().split("-")[0] for item in self.pairs if item.get("name").lower() == crypto.lower() ][0]
        return symbol
    
    
    def download(self, crypto):
        try:
            return yf.download(f"{crypto}", self.date_init, self.date_now)
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
            if result:
                results.append(pd.DataFrame(result.Close).rename(columns = {'Close': crypto.get('pair').split('-')[0]}))
        return results
    
    
    def join_dataframe(self, data_frame):
        return reduce(lambda left,right: pd.merge(left, right, on = 'Date', how = 'inner'), data_frame)
    
    
    def df_corr_to_json(self, data_frame):
        return data_frame.corr().to_json()


    def main(self):
        try:
            download = self.download_all_crypto_dataframe()
            if download:
                join_dataframe = self.join_dataframe(download)
                return self.df_corr_to_json(join_dataframe)
            
        except Exception as err:
            print(f"ERROR: {err}")