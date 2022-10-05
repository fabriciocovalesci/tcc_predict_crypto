import httpx
import locale
import re
from app.config import IMG_PLOT
from app.utils.helpers import Helper

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')


class Client(Helper):
    
    def __init__(self, crypto):
        super().__init__()
        self.api = "https://api.coingecko.com/api/v3/"
        self.crypto = crypto
          
    
    @property
    def crypto(self):
        return self._crypto
    
    
    @crypto.setter
    def crypto(self, value):
        if re.search(r"\s", value):
            self._crypto = value.replace(" ", "_")
        self._crypto = value
    
    
    def request_coingecko(self, id_crypto):
        try:
            endpoint = f"simple/price?ids={id_crypto}&vs_currencies=usd"
            resp = httpx.get(f"{self.api}{endpoint}")
            if resp.status_code == 200:
                return resp.json()
        except httpx.RequestError as err:
            print(f"ERROR ", err)
            
            
    def get_price_coin(self):
        id = [item.get("id") for item in self.pairs if item.get("name").lower() == self.crypto.lower()][0]
        # if body:
        #     return self.request_coingecko(id)
        if True:
            response = self.request_coingecko(id)
            if response and isinstance(response.get(id, None), dict) and isinstance(response.get(id).get("usd", None), float):
                return  locale.currency(response.get(id).get("usd"), grouping=True, symbol=True, international=True)
        return f"nada-{self.crypto}"
    