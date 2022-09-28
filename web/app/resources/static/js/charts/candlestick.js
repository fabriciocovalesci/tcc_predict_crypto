

async function candlestick(series, idHTML) {
    try {
        var options = {
            series: [{
                data: series
            }],
            chart: {
                type: 'candlestick',
                height: 290,
                id: 'candles',
                toolbar: {
                    autoSelected: 'pan',
                    show: false
                },
                zoom: {
                    enabled: false
                },
            },
            plotOptions: {
                candlestick: {
                    colors: {
                        upward: '#3C90EB',
                        downward: '#DF7D46'
                    }
                }
            },
            xaxis: {
                type: 'datetime'
            }
        };
        var chart = new ApexCharts(document.querySelector(`#${idHTML}`), options);
        chart.render();
    } catch (error) {

    }
};