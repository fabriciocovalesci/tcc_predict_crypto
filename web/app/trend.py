from tradingview_ta import TA_Handler, Interval, Exchange
from app.utils.helpers import Helper

class Trend(Helper):
    
    def __init__(self):
        super().__init__()
        
        
    def trend_crypto(self):
        try:
            for item in range(0, len(self.pairs)):
                symbol = self.pairs[item].get("pair").replace("-", "")
                if symbol != "DAIUSD":
                    trend = TA_Handler(
                        symbol=self.pairs[item].get("pair").replace("-", ""),
                        screener="CRYPTO",
                        exchange="BINANCE",
                        interval=Interval.INTERVAL_1_DAY,
                    )
                self.pairs[item]["trend"] = dict(trend.get_analysis().summary).get("RECOMMENDATION")
            return self.pairs
        except Exception as e:
            print(e)

        