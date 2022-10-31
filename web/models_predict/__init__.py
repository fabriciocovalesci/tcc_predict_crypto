import joblib
import sklearn
import os
import datetime
from datetime import datetime, timedelta
import pandas as pd
import yfinance as yf
from app.client import Client

class Features:
    
    @staticmethod
    def get_features(symbol):
        features = [
            { 'symbol_dai' : ['mm7d','volume', 'open'] },
            { 'symbol_matic' : ['volume','high', 'low', 'open', 'mm21d'] },
            { 'symbol_dot' : ['volume','high', 'low', 'open', 'mm21d'] },
            { 'symbol_doge' : ['volume','high', 'low', 'open', 'mm21d'] },
            { 'symbol_sol' : ['volume', 'high', 'low', 'open', 'mm21d'] },
            { 'symbol_bnb' : ['mm7d','Low', 'Volume'] },
            { 'symbol_xrp' : ['volume', 'high', 'low', 'open', 'mm21d'] },
            { 'symbol_ada' : ['volume','high', 'low', 'open', 'mm21d'] },
            { 'symbol_eth' : ['volume','high', 'low', 'open', 'mm21d'] },
            { 'symbol_btc' : ['mm21d','high', 'volume', 'low', 'open'] }  
        ]
        ticker = [ticker for ticker in features if ticker.get(f"symbol_{symbol}")][0]
        return ticker[f"symbol_{symbol}"]



class PricePredictor(Client):
    
    def __init__(self, crypto):
        super().__init__(crypto)
        self.crypto = crypto
        self.day_predict = datetime.strftime(datetime.now() + timedelta(days=1) , '%d/%m/%Y')
        self.features = Features.get_features(self.crypto.lower())       
        dir_model = os.path.abspath(__name__)
        path_model = os.path.join(dir_model, "models", f"model_{crypto}_usd.pkl")
        with open(path_model, "rb",) as load_model:
            try:
                self.model = joblib.load(load_model)
            except (OSError, FileNotFoundError, TypeError):
                exit(-1)
        

    def __str__(self):
        return self.crypto
    
             
    def predict_price(self):
        df = self.create_data_frame()
        predict_price = self.model.predict(df.tail(1)[self.features])
        return { "day_predict": self.day_predict, "price_current": float(df.tail(1)["close"]), "price_predict": predict_price[0] }
                    
                