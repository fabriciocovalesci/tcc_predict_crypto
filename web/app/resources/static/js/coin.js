
const BASE_URL = "http://127.0.0.1:5000"

const url = new URL(window.location.href);

let cryptos = [
        {"name": "Bitcoin", "par": "BTC-USD", "id": "bitcoin"},
        {"name": "Ethereum", "par": "ETH-USD", "id": "ethereum"},
        {"name": "Binance_Coin", "par": "BNB-USD", "id": "binancecoin"},
        {"name": "Ripple", "par": "XRP-USD",  "id": "ripple"},
        {"name": "Cardano", "par": "ADA-USD", "id": "cardano"},
        {"name": "Solana", "par": "SOL-USD", "id": "solana"},
        {"name": "Dogecoin", "par": "DOGE-USD",  "id": "dogecoin"},
        {"name": "Polkadot", "par": "DOT-USD",  "id": "polkadot"},
        {"name": "Polygon", "par": "MATIC-USD", "id": "matic-network"},
        {"name": "Dai", "par": "DAI-USD", "id": "dai"}
]


const crypto_id = cryptos.filter(elem => {
  if (url.pathname.replace("/coin/", "").toLowerCase().replace(/\s/g, '').includes('binance')){
    return elem
  }
   if (elem.name.toLocaleLowerCase() === url.pathname.replace("/coin/", "").toLowerCase().replace(/\s/g, '')){
    return elem
  }
});


const formatter = new Intl.NumberFormat('en-US', {
  style: 'currency',
  currency: 'USD',
  minimumFractionDigits: 4,
  maximumFractionDigits: 4, 
});



async function loadData(days){
  let dataOHLC = await getOHLC(crypto_id[0].id,  days)
  if (dataOHLC){
    $("#chart-candlestick-coin").empty();
    await candlestick(dataOHLC, 'chart-candlestick-coin')
  }
}

$("#btnradio1").change(async function(){
  if($(this).prop("checked") == true){
    await loadData($('#btnradio1').val());
  }
});

$("#btnradio7").change(async function(){
  if($(this).prop("checked") == true){
    await loadData($('#btnradio7').val());
  }
});


$("#btnradio14").change(async function(){
  if($(this).prop("checked") == true){
    await loadData($('#btnradio14').val());
  }
});


$("#btnradio30").change(async function(){
  if($(this).prop("checked") == true){
    await loadData($('#btnradio30').val());
  }
});


$("#btnradio90").change(async function(){
  if($(this).prop("checked") == true){
    await loadData($('#btnradio90').val());
  }
});

$("#btnradio180").change(async function(){
  if($(this).prop("checked") == true){
    await loadData($('#btnradio180').val());
  }
});

$("#btnradio365").change(async function(){
  if($(this).prop("checked") == true){
    await loadData($('#btnradio365').val());
  }
});

$("#btnradiomax").change(async function(){
  if($(this).prop("checked") == true){
    await loadData($('#btnradiomax').val());
  }
});


$(window).on('load', async function() {
  document.getElementById("price-current").innerHTML = formatter.format(document.getElementById("price-current").textContent);
  document.getElementById("price-predict").innerHTML = formatter.format(document.getElementById("price-predict").textContent);
  await loadData(1);
})
