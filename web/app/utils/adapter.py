import pandas as pd

class Adapter:
    
    def __init__(self, process):
        self.process = process
        self.columns = ['timestamp', "low", "high", "open", "close", "volume"]
        
        
    def remane_columns(self, new_df):
        if list(new_df.columns) != self.columns:
            new_df.rename({'Date': 'timestamp', 'Open': 'open', 'High': 'high', 'Low': 'low', 'Adj Close': 'close', 'Volume': 'volume' }, axis=1, inplace=True)


    def clean_data(self, new_df):
        new_df.dropna(inplace=True)
        
        
    def transform(self, new_df):
        if isinstance(new_df, list):
            new_df = pd.DataFrame(data=new_df, columns=self.columns)
            return new_df

        
    def handle(self, new_df):
        if isinstance(new_df, list):
            new_df = self.transform(new_df)
        self.remane_columns(new_df)
        self.clean_data(new_df)
        message = {
            "timestamp": pd.to_datetime(new_df['timestamp'], unit='s'),
            "open": new_df["open"],
            "high": new_df["high"],
            "low": new_df["low"],
            "close": new_df["close"],
            "volume": new_df["volume"],
            "mm7d": new_df['close'].rolling(7).mean(),
            "mm21d": new_df['close'].rolling(21).mean()
        }
        response = self.process.handle(message)
        return response
    

class Code():
    
    def handle(self, message):
        return pd.DataFrame(message)