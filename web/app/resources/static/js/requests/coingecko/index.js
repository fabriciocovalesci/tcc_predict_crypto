

const BASE_URL_API = "https://api.coingecko.com/api/v3/"
const BASE_URL_API_COIN_BASE = "https://api.exchange.coinbase.com/products"


const products = {
    "bitcoin": "BTC",
    "ethereum": "ETH",
    "binancecoin": "BNB",
    "ripple": "XRP",
    "cardano": "ADA",
    "solana": "SOL",
    "dogecoin": "DOGE",
    "polkadot": "DOT",
    "matic-network": "MATIC",
    "dai": "DAI"
}


async function getPriceCryptoCoinCase(crypto) {
    try { 
        let headers = { accept: 'application/json'}
        const resp = await axios.get(`${BASE_URL_API_COIN_BASE}/${products[crypto]}-USD/ticker`, headers);
        return resp.data.price;
    } catch (err) {
        console.error(err);
    }
}


async function getPriceCryptoCoinGecko(crypto) {
    try {
        let headers = { accept: 'application/json'}
        const resp = await axios.get(`${BASE_URL_API}simple/price?ids=${crypto}&vs_currencies=usd`, headers);
        return resp.data[crypto].usd;
    } catch (err) {
        console.error(err);
    }
};


async function getPriceCrypto(crypto) {
    try {
        let price = 0.0;
        if (crypto === "ripple" || crypto === "binancecoin") {
            price = await getPriceCryptoCoinGecko(crypto);
        }else {
            price = await getPriceCryptoCoinCase(crypto);
        }
        return format_currency(price)
    } catch (err) {
        console.error(err);
    }
};


async function getOHLC(crypto, days) {
    try {
        if (crypto && days) {
            const resp = await axios.get(`${BASE_URL_API}coins/${crypto}/ohlc?vs_currency=usd&days=${days}`);
            if (typeof resp.data !== undefined){
                return resp.data;
            }else return []
        }
    } catch (err) {
        console.error(err);
    }
};