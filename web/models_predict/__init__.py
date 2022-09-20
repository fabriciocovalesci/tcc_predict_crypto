import pickle
import os
import datetime
import pandas as pd


class PricePredictor:
    
    def __init__(self, today, days, crypto):
        self.prev_date = today
        self.next_date = ""
        self.days = days
        dir_model = os.path.abspath(__name__)
        path_model = os.path.join(dir_model, f"model_{crypto}_usd.pckl")
        with open(path_model, "rb",) as load_model:
            try:
                self.model = pickle.load(load_model)
            except (OSError, FileNotFoundError, TypeError):
                print("wrong path/ model not available")
                exit(-1)
                
    def calculate_next_date(self):
        """
        Calculates next date
        date_format = yyyy-mm-dd
        """
        self.next_date = datetime.datetime(
            *list(map(lambda x: int(x), self.prev_date.split("-")))
        ) + datetime.timedelta(
            days=int(self.days)
        )
    
    def get_next_date(self):
        try:
            return self.next_date.strftime("%Y-%m-%d")
        except NameError:
            self.calculate_next_date()
            
            
    def generate_days(self):
        list_days = []
        for day in range(self.days+1):
            previous_date = datetime.datetime.today() + datetime.timedelta(days=day)
            list_days.append(previous_date.strftime("%Y-%m-%d"))
        return list_days
    
    
    def merge_price_prediction(self, pred):
        list_days = self.generate_days()
        list_merge = []
        for idx, price in enumerate(pred):
            for index, day in enumerate(list_days):
                if idx == index:
                    list_merge.append({
                        "day": day,
                        "price": price
                    })
        return list_merge
            
                
    def preprocess_inputs(self):
        """
        Model takes in an input as a pandas dataframe having index 
        as the day to be predicted
        """
        self.calculate_next_date() 
        next_date_series = pd.DataFrame(
            {"ds": pd.date_range(start=self.prev_date, end=self.next_date)}
        )
        return next_date_series
    
    
    def postprocess_outputs(self, output_from_model):
        """
        Return the yhat in the list format
        """
        return output_from_model["yhat"].tolist()

    
    def predict(self):
        next_date_series = self.preprocess_inputs() 
        pred = self.model.predict(next_date_series) 
        pred = self.postprocess_outputs(pred)
        prediction = self.merge_price_prediction(pred)
        return prediction 
