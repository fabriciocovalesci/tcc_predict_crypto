Apex.grid = {
    padding: {
      right: 0,
      left: 0
    }
  }
  
  Apex.dataLabels = {
    enabled: false
  }
  
  var randomizeArray = function (arg) {
    var array = arg.slice();
    var currentIndex = array.length, temporaryValue, randomIndex;
  
    while (0 !== currentIndex) {
  
      randomIndex = Math.floor(Math.random() * currentIndex);
      currentIndex -= 1;
  
      temporaryValue = array[currentIndex];
      array[currentIndex] = array[randomIndex];
      array[randomIndex] = temporaryValue;
    }
  
    return array;
  }
  
  // data for the sparklines that appear below header area
  var sparklineData = [47, 45, 54, 38, 56, 24, 65, 31, 37, 39, 62, 51, 35, 41, 35, 27, 93, 53, 61, 27, 54, 43, 19];

  let btc = [20127.14,
    19969.77,
    19832.09,
    19986.71,
    19812.37,
    18837.67,
    19290.32,
    19329.83,
    21381.15,
    21680.54,
    21769.26,
    22370.45,
    20296.71,
    20241.09,
    19701.21,
    19772.58,
    20127.58,
    19419.51,
    19544.13,
    18890.79,
    18547.4,
    19413.55]

    let ethereum = [1586.18,
      1577.22,
      1556.87,
      1577.64,
      1617.18,
      1561.75,
      1629.91,
      1635.35,
      1719.09,
      1776.2,
      1761.8,
      1713.77,
      1580.79,
      1634.76,
      1471.69,
      1432.45,
      1469.74,
      1335.33,
      1377.54,
      1324.39,
      1252.61,
      1327.68]

    let solana = [31.59,
      31.23,
      31.11,
      32.11,
      32.19,
      30.89,
      32.71,
      33.61,
      34.74,
      35.13,
      34.97,
      37.42,
      33.43,
      34.09,
      33.05,
      32.21,
      33.75,
      31.06,
      32.69,
      31.43,
      30.83,
      32.41]
  
  // the default colorPalette for this dashboard
  //var colorPalette = ['#01BFD6', '#5564BE', '#F7A600', '#EDCD24', '#F74F58'];
  var colorPalette = ['#00D8B6','#008FFB',  '#FEB019', '#FF4560', '#775DD0']
  

  var date = new Date();
  //+"-"+ date.getDate()
	var current_date = date.getFullYear()+"-"+(date.getMonth()+1);
  var spark1 = {
    chart: {
      id: 'sparkline1',
      group: 'sparklines',
      type: 'area',
      height: 160,
      sparkline: {
        enabled: true
      },
    },
    stroke: {
      curve: 'straight'
    },
    fill: {
      opacity: 1,
    },
    series: [{
      name: 'Bitcoin',
      data: btc
    }],
    labels: [...Array(23).keys()].map(n => `${current_date}-${n+1}`),
    yaxis: {
      min: 0
    },
    xaxis: {
      type: 'datetime',
    },
    colors:['#00aeef'],
    title: {
      text: '$424,652',
      offsetX: 30,
      style: {
        fontSize: '24px',
        cssClass: 'apexcharts-yaxis-title'
      }
    },
    subtitle: {
      text: 'Bitcoin',
      offsetX: 30,
      style: {
        fontSize: '14px',
        cssClass: 'apexcharts-yaxis-title'
      }
    }
  }
  
  var spark2 = {
    chart: {
      id: 'sparkline2',
      group: 'sparklines',
      type: 'area',
      height: 160,
      sparkline: {
        enabled: true
      },
    },
    stroke: {
      curve: 'straight'
    },
    fill: {
      opacity: 1,
    },
    series: [{
      name: 'Ethereum',
      data: ethereum
    }],
    labels: [...Array(23).keys()].map(n => `${current_date}-${n+1}`),
    yaxis: {
      min: 0
    },
    xaxis: {
      type: 'datetime',
    },
    colors: ['#979be8'],
    title: {
      text: '$235,312',
      offsetX: 30,
      style: {
        fontSize: '24px',
        cssClass: 'apexcharts-yaxis-title'
      }
    },
    subtitle: {
      text: 'Ethereum',
      offsetX: 30,
      style: {
        fontSize: '14px',
        cssClass: 'apexcharts-yaxis-title'
      }
    }
  }
  
  var spark3 = {
    chart: {
      id: 'sparkline3',
      group: 'sparklines',
      type: 'area',
      height: 160,
      sparkline: {
        enabled: true
      },
    },
    stroke: {
      curve: 'straight'
    },
    fill: {
      opacity: 1,
    },
    series: [{
      name: 'Solana',
      data: solana
    }],
    labels:[...Array(23).keys()].map(n => `${current_date}-${n+1}`),
    xaxis: {
      type: 'datetime',
    },
    yaxis: {
      min: 0
    },
    colors: ['#008FFB'],
    //colors: ['#5564BE'],
    title: {
      text: '$135,965',
      offsetX: 30,
      style: {
        fontSize: '24px',
        cssClass: 'apexcharts-yaxis-title'
      }
    },
    subtitle: {
      text: 'Solana',
      offsetX: 30,
      style: {
        fontSize: '14px',
        cssClass: 'apexcharts-yaxis-title'
      }
    }
  }
  
  var monthlyEarningsOpt = {
    chart: {
      type: 'area',
      height: 260,
      background: '#eff4f7',
      sparkline: {
        enabled: true
      },
      offsetY: 20
    },
    stroke: {
      curve: 'straight'
    },
    fill: {
      type: 'solid',
      opacity: 1,
    },
    series: [{
      data: randomizeArray(sparklineData)
    }],
    xaxis: {
      crosshairs: {
        width: 1
      },
    },
    yaxis: {
      min: 0,
      max: 130
    },
    colors: ['#dce6ec'],
  
    title: {
      text: 'Total Earned',
      offsetX: -30,
      offsetY: 100,
      align: 'right',
      style: {
        color: '#7c939f',
        fontSize: '16px',
        cssClass: 'apexcharts-yaxis-title'
      }
    },
    subtitle: {
      text: '$135,965',
      offsetX: -30,
      offsetY: 100,
      align: 'right',
      style: {
        color: '#7c939f',
        fontSize: '24px',
        cssClass: 'apexcharts-yaxis-title'
      }
    }
  }
  
  
  new ApexCharts(document.querySelector("#spark1"), spark1).render();
  new ApexCharts(document.querySelector("#spark2"), spark2).render();
  new ApexCharts(document.querySelector("#spark3"), spark3).render();
  
  var monthlyEarningsChart = new ApexCharts(document.querySelector("#monthly-earnings-chart"), monthlyEarningsOpt);
  
  
  var optionsArea = {
    chart: {
      height: 340,
      type: 'area',
      zoom: {
        enabled: false
      },
    },
    stroke: {
      curve: 'straight'
    },
    colors: colorPalette,
    series: [
      {
        name: "Blog",
        data: [{
          x: 0,
          y: 0
        }, {
          x: 4,
          y: 5
        }, {
          x: 5,
          y: 3
        }, {
          x: 9,
          y: 8
        }, {
          x: 14,
          y: 4
        }, {
          x: 18,
          y: 5
        }, {
          x: 25,
          y: 0
        }]
      },
      {
        name: "Social Media",
        data: [{
          x: 0,
          y: 0
        }, {
          x: 4,
          y: 6
        }, {
          x: 5,
          y: 4
        }, {
          x: 14,
          y: 8
        }, {
          x: 18,
          y: 5.5
        }, {
          x: 21,
          y: 6
        }, {
          x: 25,
          y: 0
        }]
      },
      {
        name: "External",
        data: [{
          x: 0,
          y: 0
        }, {
          x: 2,
          y: 5
        }, {
          x: 5,
          y: 4
        }, {
          x: 10,
          y: 11
        }, {
          x: 14,
          y: 4
        }, {
          x: 18,
          y: 8
        }, {
          x: 25,
          y: 0
        }]
      }
    ],
    fill: {
      opacity: 1,
    },
    title: {
      text: 'Daily Visits Insights',
      align: 'left',
      style: {
        fontSize: '18px'
      }
    },
    markers: {
      size: 0,
      style: 'hollow',
      hover: {
        opacity: 5,
      }
    },
    tooltip: {
      intersect: true,
      shared: false,
    },
    xaxis: {
      tooltip: {
        enabled: false
      },
      labels: {
        show: false
      },
      axisTicks: {
        show: false
      }
    },
    yaxis: {
      tickAmount: 4,
      max: 12,
      axisBorder: {
        show: false
      },
      axisTicks: {
        show: false
      },
      labels: {
        style: {
          colors: '#78909c'
        }
      }
    },
    legend: {
      show: false
    }
  }
  
  var chartArea = new ApexCharts(document.querySelector('#area'), optionsArea);
  chartArea.render();
  
  var optionsBar = {
    chart: {
      type: 'bar',
      height: 380,
      width: '100%',
      stacked: true,
    },
    plotOptions: {
      bar: {
        columnWidth: '45%',
      }
    },
    colors: colorPalette,
    series: [{
      name: "Clothing",
      data: [42, 52, 16, 55, 59, 51, 45, 32, 26, 33, 44, 51, 42, 56],
    }, {
      name: "Food Products",
      data: [6, 12, 4, 7, 5, 3, 6, 4, 3, 3, 5, 6, 7, 4],
    }],
    labels: [10,11,12,13,14,15,16,17,18,19,20,21,22,23],
    xaxis: {
      labels: {
        show: false
      },
      axisBorder: {
        show: false
      },
      axisTicks: {
        show: false
      },
    },
    yaxis: {
      axisBorder: {
        show: false
      },
      axisTicks: {
        show: false
      },
      labels: {
        style: {
          colors: '#78909c'
        }
      }
    },
    title: {
      text: 'Monthly Sales',
      align: 'left',
      style: {
        fontSize: '18px'
      }
    }
  
  }
  
  var chartBar = new ApexCharts(document.querySelector('#bar'), optionsBar);
  chartBar.render();
  
  
  var optionDonut = {
    chart: {
        type: 'donut',
        width: '100%',
        height: 400
    },
    dataLabels: {
      enabled: false,
    },
    plotOptions: {
      pie: {
        customScale: 0.8,
        donut: {
          size: '75%',
        },
        offsetY: 20,
      },
      stroke: {
        colors: undefined
      }
    },
    colors: colorPalette,
    title: {
      text: 'Department Sales',
      style: {
        fontSize: '18px'
      }
    },
    series: [21, 23, 19, 14, 6],
    labels: ['Clothing', 'Food Products', 'Electronics', 'Kitchen Utility', 'Gardening'],
    legend: {
      position: 'left',
      offsetY: 80
    }
  }
  
  var donut = new ApexCharts(
    document.querySelector("#donut"),
    optionDonut
  )
  donut.render();
  
  
  function trigoSeries(cnt, strength) {
    var data = [];
    for (var i = 0; i < cnt; i++) {
        data.push((Math.sin(i / strength) * (i / strength) + i / strength+1) * (strength*2));
    }
  
    return data;
  }
  
  
  
  var optionsLine = {
    chart: {
      height: 340,
      type: 'line',
      zoom: {
        enabled: false
      }
    },
    plotOptions: {
      stroke: {
        width: 4,
        curve: 'smooth'
      },
    },
    colors: colorPalette,
    series: [
      {
        name: "Day Time",
        data: trigoSeries(52, 20)
      },
      {
        name: "Night Time",
        data: trigoSeries(52, 27)
      },
    ],
    title: {
      floating: false,
      text: 'Customers',
      align: 'left',
      style: {
        fontSize: '18px'
      }
    },
    subtitle: {
      text: '168,215',
      align: 'center',
      margin: 30,
      offsetY: 40,
      style: {
        color: '#222',
        fontSize: '24px',
      }
    },
    markers: {
      size: 0
    },
  
    grid: {
  
    },
    xaxis: {
      labels: {
        show: false
      },
      axisTicks: {
        show: false
      },
      tooltip: {
        enabled: false
      }
    },
    yaxis: {
      tickAmount: 2,
      labels: {
        show: false
      },
      axisBorder: {
        show: false,
      },
      axisTicks: {
        show: false
      },
      min: 0,
    },
    legend: {
      position: 'top',
      horizontalAlign: 'left',
      offsetY: -20,
      offsetX: -30
    }
  
  }
  
  var chartLine = new ApexCharts(document.querySelector('#line'), optionsLine);
  
  // a small hack to extend height in website sample dashboard
  chartLine.render().then(function () {
    var ifr = document.querySelector("#wrapper");
    if (ifr.contentDocument) {
      ifr.style.height = ifr.contentDocument.body.scrollHeight + 20 + 'px';
    }
  });
  
  
  // on smaller screen, change the legends position for donut
  var mobileDonut = function() {
    if($(window).width() < 768) {
      donut.updateOptions({
        plotOptions: {
          pie: {
            offsetY: -15,
          }
        },
        legend: {
          position: 'bottom'
        }
      }, false, false)
    }
    else {
      donut.updateOptions({
        plotOptions: {
          pie: {
            offsetY: 20,
          }
        },
        legend: {
          position: 'left'
        }
      }, false, false)
    }
  }
  
  $(window).resize(function() {
    mobileDonut()
  });






  function generateData(count, yrange) {
    var i = 0;
    var series = [];
    while (i < count) {
      var x = (i + 1).toString();
      var y =
        Math.floor(Math.random() * (yrange.max - yrange.min + 1)) + yrange.min;
  
      series.push({
        x: x,
        y: y
      });
      i++;
    }
    return series;
  }
  
  var options = {
    chart: {
      height: 350,
      type: "heatmap"
    },
    colors: [
      "#5A9BD5",
      "#5A9BD5",
      "#5A9BD5",
      "#5A9BD5",
      "#ffffff",
      "#F8C045",
      "#F8C045",
      "#F8C045",
      "#F8C045"
    ],
    plotOptions: {
      heatmap: {
        shadeIntensity: 1
      }
    },
    dataLabels: {
      enabled: true
    },
    series: [
      {
        name: "Bitcoin",
        data: generateData(20, {
          min: -30,
          max: 55
        })
      },
      {
        name: "Ethereum",
        data: generateData(20, {
          min: -30,
          max: 55
        })
      },
      {
        name: "Mar",
        data: generateData(20, {
          min: -30,
          max: 55
        })
      },
      {
        name: "Apr",
        data: generateData(20, {
          min: -30,
          max: 55
        })
      },
      {
        name: "",
        data: generateData(20, {
          min: 0,
          max: 0
        })
      },
      {
        name: "May",
        data: generateData(20, {
          min: -30,
          max: 55
        })
      },
      {
        name: "Jun",
        data: generateData(20, {
          min: -30,
          max: 55
        })
      },
      {
        name: "Jul",
        data: generateData(20, {
          min: -30,
          max: 55
        })
      },
      {
        name: "Aug",
        data: generateData(20, {
          min: -30,
          max: 55
        })
      }
    ],
    tooltip: {
      custom: function({ series, seriesIndex, dataPointIndex, w }) {
        if (w.globals.seriesNames[seriesIndex] !== "") {
          return series[seriesIndex][dataPointIndex]+" ab";
        } else {
          return "";
        }
      }
    }
  };
  
  var chartheatmap = new ApexCharts(document.querySelector("#chart-HeatMap"), options);
  
  chartheatmap.render();



