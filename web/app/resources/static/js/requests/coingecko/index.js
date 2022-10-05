

const BASE_URL_API = "https://api.coingecko.com/api/v3/"



async function getPriceCrypto(crypto) {
    try {
        const resp = await axios.get(`${BASE_URL_API}simple/price?ids=${crypto}&vs_currencies=usd`);
        return format_currency(resp.data[crypto].usd)
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