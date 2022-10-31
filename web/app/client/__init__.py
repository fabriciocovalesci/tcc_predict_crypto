import httpx
import locale
import re
import pandas as pd
from datetime import datetime, timedelta
from app.config import IMG_PLOT
from app.utils.helpers import Helper
from app.utils.adapter import Adapter, Code
import yfinance as yf

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')


class Client(Helper):
    
    def __init__(self, crypto):
        super().__init__()
        self.crypto = crypto.upper()
        self.api = "https://api.exchange.coinbase.com/"
        self.granularity = 86400
        self.start_date = datetime.strftime(datetime.now() + timedelta(days=-30) , '%Y-%m-%dT00:00:00')
        self.end_date = datetime.strftime(datetime.now() , '%Y-%m-%dT23:59:59')
        self.day_predict = datetime.strftime(datetime.now() + timedelta(days=1) , '%d/%m/%Y')
        self.date_now = datetime.strftime(datetime.now() , '%Y-%m-%d')
        self.day50 = datetime.strftime(datetime.now() + timedelta(days=-50) , '%Y-%m-%d')
        self.params = { "start": self.start_date, "end": self.end_date, "granularity": self.granularity }
        self.columns = ['timestamp', "low", "high", "open", "close", "volume"]
               
    
    def request_coinbase(self):
        try:
            if self.crypto not in "XRP,BNB".split(","):
                endpoint = f"products/{self.crypto}-USD/candles"
                resp = httpx.get(f"{self.api}{endpoint}", params=self.params, headers={"content-type": "application/json"})
                if resp.status_code == 200:
                    data = list(reversed(list(resp.json())))
                    return data
            return None
        except httpx.RequestError as err:
            print(f"ERROR ", err)
            
            
    def request_yahoo(self):
        if self.crypto.upper() in "XRP,BNB".split(","):
            new_df = yf.download(f"{self.crypto}-USD", self.day50, self.date_now, progress=False)
            new_df.reset_index(inplace=True)
            return new_df
            
            
    def create_data_frame(self):
        try:
            if self.crypto.upper() in "XRP,BNB".split(","):
                data = self.request_yahoo()
            elif self.crypto.upper() not in "XRP,BNB".split(","):
                data = self.request_coinbase()
            else:
                data = None
            new_df = Adapter(Code())
            new_df = new_df.handle(data)
            return new_df
        except Exception as err:
            print(f"ERROR {err}")            
    
    