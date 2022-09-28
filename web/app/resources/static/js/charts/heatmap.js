
function correlationHeatMap(data_crypto){
    let corr = []
        Object.values(data_crypto).filter(el => {
            corr.push(Object.values((el)));
        })

        let xValues = Object.keys(data_crypto)
        let yValues = Object.keys(data_crypto)
        let zValues = [...corr]

        var data = [{
            x: xValues,
            y: yValues,
            z: zValues,
            type: 'heatmap',
            showscale: true,
            colorscale: "BrBG",

        }];

        var layout = {
            title: 'Gráfico de Correlação',
            annotations: [],
            xaxis: {
                ticks: 'top',
                side: 'top'
            },
            yaxis: {
                ticks: 'top',
                ticksuffix: ' ',
                width: 700,
                height: 700,
                autosize: false
            }
        };

        for (var i = 0; i < yValues.length; i++) {
            for (var j = 0; j < xValues.length; j++) {
                var currentValue = zValues[i][j];
                if (currentValue != 0.0) {
                    var textColor = 'white';
                } else {
                    var textColor = 'black';
                }
                var result = {
                    xref: 'x1',
                    yref: 'y1',
                    x: xValues[j],
                    y: yValues[i],
                    text: (zValues[i][j].toFixed(2)),
                    font: {
                        family: 'Arial',
                        size: 12,
                        color: 'rgb(50, 171, 96)'
                    },
                    showarrow: false,
                    font: {
                        color: textColor
                    }
                };
                layout.annotations.push(result);
            }
        }

        Plotly.newPlot('chart-heatmap', data, layout);
}