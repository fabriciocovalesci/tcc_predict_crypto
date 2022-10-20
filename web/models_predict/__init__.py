import joblib
import sklearn
import os
import datetime
from datetime import datetime, timedelta
import pandas as pd
import yfinance as yf


class Features:
    
    
    @staticmethod
    def get_features(symbol):
        features = [
            { 'symbol_dai' : ['mm7d','High', 'Open'] },
            { 'symbol_matic' : ['mm7d','Low', 'Volume', 'High', 'Open', 'mm21d'] },
            { 'symbol_dot' : ['mm7d','Low', 'Volume', 'High', 'mm21d', 'Open'] },
            { 'symbol_doge' : ['mm7d','Low', 'Volume', 'High'] },
            { 'symbol_sol' : ['mm7d', 'Low', 'Volume', 'High', 'mm21d', 'Open'] },
            { 'symbol_bnb' : ['mm7d','Low', 'Volume'] },
            { 'symbol_xrp' : ['mm7d','Low', 'Volume', 'High', 'mm21d', 'Open'] },
            { 'symbol_ada' : ['mm7d','Low', 'Volume', 'High', 'mm21d', 'Open'] },
            { 'symbol_eth' : ['mm7d','Low', 'Volume', 'High', 'Open', 'mm21d'] },
            { 'symbol_btc' : ['mm7d','mm21d', 'Volume', 'High', 'Low'] }  
        ]
        ticker = [ticker for ticker in features if ticker.get(f"symbol_{symbol}")][0]
        return ticker[f"symbol_{symbol}"]



class PricePredictor:
    
    def __init__(self, crypto):
        self.crypto = crypto
        self.day_predict = datetime.strftime(datetime.now() + timedelta(days=1) , '%d/%m/%Y')
        self.day7 = datetime.strftime(datetime.now() + timedelta(days=-7) , '%Y-%m-%d')
        self.day50 = datetime.strftime(datetime.now() + timedelta(days=-50) , '%Y-%m-%d')
        self.date_now = datetime.strftime(datetime.now() , '%Y-%m-%d')
        self.features = Features.get_features(self.crypto.lower())
        self.df = yf.download(f"{self.crypto}-USD", self.day50, self.date_now, progress=False)
        self.df['mm7d'] = self.df['Adj Close'].rolling(7).mean()
        self.df['mm21d'] = self.df['Adj Close'].rolling(21).mean()
        self.df.dropna(inplace=True)
        self.df.reset_index(inplace=True)
        self.price_current = float(self.df.tail(1)["Adj Close"])
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
        predict_price = self.model.predict(self.df.tail(1)[self.features])
        return { "day_predict": self.day_predict, "price_current": self.price_current, "price_predict": predict_price[0] }
                    
                

                
    # def calculate_next_date(self):
    #     self.next_date = datetime.datetime(
    #         *list(map(lambda x: int(x), self.prev_date.split("-")))
    #     ) + datetime.timedelta(
    #         days=int(self.days)
    #     )
    
    
    
    # def get_next_date(self):
    #     try:
    #         return self.next_date.strftime("%Y-%m-%d")
    #     except NameError:
    #         self.calculate_next_date()
            
            
    # def generate_days(self):
    #     list_days = []
    #     for day in range(self.days+1):
    #         previous_date = datetime.datetime.today() + datetime.timedelta(days=day)
    #         list_days.append(previous_date.strftime("%Y-%m-%d"))
    #     return list_days
    
    
    # def merge_price_prediction(self, pred):
    #     list_days = self.generate_days()
    #     list_merge = []
    #     for idx, price in enumerate(pred):
    #         for index, day in enumerate(list_days):
    #             if idx == index:
    #                 list_merge.append({
    #                     "day": day,
    #                     "price": price
    #                 })
    #     return list_merge
            
                
    # def preprocess_inputs(self):
    #     self.calculate_next_date() 
    #     next_date_series = pd.DataFrame(
    #         {"ds": pd.date_range(start=self.prev_date, end=self.next_date)}
    #     )
    #     return next_date_series
    
    
    # def postprocess_outputs(self, output_from_model):
    #     return output_from_model["yhat"].tolist()

    
    # def predict(self):
    #     predict2 = self.model.predict(self.df[])
    #     next_date_series = self.preprocess_inputs() 
    #     pred = self.model.predict(next_date_series) 
    #     pred = self.postprocess_outputs(pred)
    #     prediction = self.merge_price_prediction(pred)
    #     return prediction 


"""
     
"""