




window.addEventListener("load", async function(){
  let ids = ["bitcoin", "ethereum", "binancecoin", "ripple", "cardano", "solana", "dogecoin", "polkadot", "matic-network", "dai"]
  ids.forEach(async(id) => {
    $(`#price-${id}`)[0].append(await getPriceCrypto(id))
  });
  let heatmap = {"BTC":{"BTC":1.0,"ETH":0.8265655044,"SOL":0.6198072895,"XRP":0.782531178,"MATIC":0.5496444679,"DOT":0.9449621327,"DOGE":0.6213520207,"DAI":-0.4329308862,"ADA":0.7957615137,"BNB":0.7778927664},"ETH":{"BTC":0.8265655044,"ETH":1.0,"SOL":0.8759797599,"XRP":0.8049700302,"MATIC":0.8761137189,"DOT":0.7805138836,"DOGE":0.7528909018,"DAI":-0.4647213664,"ADA":0.8402742076,"BNB":0.9310490976},"SOL":{"BTC":0.6198072895,"ETH":0.8759797599,"SOL":1.0,"XRP":0.5968488706,"MATIC":0.8196774324,"DOT":0.6177604163,"DOGE":0.4807734268,"DAI":-0.320645229,"ADA":0.673468311,"BNB":0.7715343516},"XRP":{"BTC":0.782531178,"ETH":0.8049700302,"SOL":0.5968488706,"XRP":1.0,"MATIC":0.6179519409,"DOT":0.7989408035,"DOGE":0.8539118847,"DAI":-0.3225630732,"ADA":0.8420893346,"BNB":0.8209496485},"MATIC":{"BTC":0.5496444679,"ETH":0.8761137189,"SOL":0.8196774324,"XRP":0.6179519409,"MATIC":1.0,"DOT":0.5011419701,"DOGE":0.6478502451,"DAI":-0.4179257142,"ADA":0.6809129117,"BNB":0.8298954567},"DOT":{"BTC":0.9449621327,"ETH":0.7805138836,"SOL":0.6177604163,"XRP":0.7989408035,"MATIC":0.5011419701,"DOT":1.0,"DOGE":0.6436114751,"DAI":-0.2935002567,"ADA":0.8133890702,"BNB":0.7448047796},"DOGE":{"BTC":0.6213520207,"ETH":0.7528909018,"SOL":0.4807734268,"XRP":0.8539118847,"MATIC":0.6478502451,"DOT":0.6436114751,"DOGE":1.0,"DAI":-0.3264312043,"ADA":0.812605952,"BNB":0.7736345988},"DAI":{"BTC":-0.4329308862,"ETH":-0.4647213664,"SOL":-0.320645229,"XRP":-0.3225630732,"MATIC":-0.4179257142,"DOT":-0.2935002567,"DOGE":-0.3264312043,"DAI":1.0,"ADA":-0.3548504328,"BNB":-0.477411309},"ADA":{"BTC":0.7957615137,"ETH":0.8402742076,"SOL":0.673468311,"XRP":0.8420893346,"MATIC":0.6809129117,"DOT":0.8133890702,"DOGE":0.812605952,"DAI":-0.3548504328,"ADA":1.0,"BNB":0.7805015851},"BNB":{"BTC":0.7778927664,"ETH":0.9310490976,"SOL":0.7715343516,"XRP":0.8209496485,"MATIC":0.8298954567,"DOT":0.7448047796,"DOGE":0.7736345988,"DAI":-0.477411309,"ADA":0.7805015851,"BNB":1.0}}

  let corr = await get_corr_home();
  correlationHeatMap(corr)
});