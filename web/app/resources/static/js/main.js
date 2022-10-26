




window.addEventListener("load", async function(){
  let ids = ["bitcoin", "ethereum", "binancecoin", "ripple", "cardano", "solana", "dogecoin", "polkadot", "matic-network", "dai"]
  ids.forEach(async(id) => {
    $(`#price-${id}`)[0].append(await getPriceCrypto(id))
  });

  correlationHeatMap(crypto_corr)
});