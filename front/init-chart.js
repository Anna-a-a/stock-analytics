function init_chart() {
const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);
const ticker = urlParams.get('ticker')

var stock = httpGet("/api/stock/" + ticker);
document.getElementById('price').innerHTML = stock.price;
document.getElementById('head-title').innerHTML = stock.name + " - " + stock.ticker;
document.getElementById('dividends-percent-forecast-yy').innerHTML = stock.netIncomePercentForecast + "%";
document.getElementById('revenue-percent-forecast').innerHTML = stock.revenuePercentForecast + "%";
document.getElementById('netIncome-percent-forecast').innerHTML = stock.netIncomePercentForecast + "%";
document.getElementById('dividends-percent-forecast').innerHTML = stock.dividendPercentToCurrentPrice + "%";

document.getElementById('dividends-percent-average').innerHTML = stock.dividendAveragePercentGrowth + "%";
document.getElementById('revenue-percent-average').innerHTML = stock.revenueAveragePercentGrowth + "%";
document.getElementById('netIncome-percent-average').innerHTML = stock.netIncomeAveragePercentGrowth + "%";


var dividendsChartOptions = {
                                   animationEnabled: true,
                            	   theme: "light2",
                                   title: {
                                       text: "Dividends"
                                   },
                                   data: [{
                                       type: "column",
                                       indexLabel: "{y}",
                                       indexLabelPlacement: "inside",
                                       indexLabelOrientation: "horizontal",
                                       color: "#5592ad",
                                       type: "column",
                                       dataPoints: stock.dividendsColumnChartData
                                   }]
                               };
var lastDataPoint = dividendsChartOptions.data[0].dataPoints[dividendsChartOptions.data[0].dataPoints.length - 1];
lastDataPoint.color = "#29a36c";
var dividendsChart = new CanvasJS.Chart("dividends-chart", dividendsChartOptions);
dividendsChart.render();


var revenueChart = new CanvasJS.Chart("revenue-chart", {
       animationEnabled: true,
	   theme: "light2",
       title: {
           text: "Revenue"
       },
        data: [
             {
                 type: "column",
                 indexLabel: "{y}",
                 indexLabelPlacement: "inside",
                 indexLabelOrientation: "horizontal",
                 type: "stackedColumn",
                 dataPoints: stock.revenueDataStackedColumnChartData.q1
             },
             {
                 type: "column",
                 indexLabel: "{y}",
                 indexLabelPlacement: "inside",
                 indexLabelOrientation: "horizontal",
                 type: "stackedColumn",
                 dataPoints: stock.revenueDataStackedColumnChartData.q2
             },
             {
                 type: "column",
                 indexLabel: "{y}",
                 indexLabelPlacement: "inside",
                 indexLabelOrientation: "horizontal",
                 type: "stackedColumn",
                 dataPoints: stock.revenueDataStackedColumnChartData.q3
             },
             {
                 type: "column",
                 indexLabel: "{y}",
                 indexLabelPlacement: "inside",
                 indexLabelOrientation: "horizontal",
                 type: "stackedColumn",
                 dataPoints: stock.revenueDataStackedColumnChartData.q4
             }
             ]
   });
revenueChart.render();

var netIncomeChart = new CanvasJS.Chart("netIncome-chart", {
       animationEnabled: true,
	   theme: "light2",
       title: {
           text: "Net income"
       },
        data: [
             {
                 type: "column",
                 indexLabel: "{y}",
                 indexLabelPlacement: "inside",
                 indexLabelOrientation: "horizontal",
                 type: "stackedColumn",
                 dataPoints: stock.netIncomeDataStackedColumnChartData.q1
             },
             {
                 type: "column",
                 indexLabel: "{y}",
                 indexLabelPlacement: "inside",
                 indexLabelOrientation: "horizontal",
                 type: "stackedColumn",
                 dataPoints: stock.netIncomeDataStackedColumnChartData.q2
             },
             {
                 type: "column",
                 indexLabel: "{y}",
                 indexLabelPlacement: "inside",
                 indexLabelOrientation: "horizontal",
                 type: "stackedColumn",
                 dataPoints: stock.netIncomeDataStackedColumnChartData.q3
             },
             {
                 type: "column",
                 indexLabel: "{y}",
                 indexLabelPlacement: "inside",
                 indexLabelOrientation: "horizontal",
                 type: "stackedColumn",
                 dataPoints: stock.netIncomeDataStackedColumnChartData.q4
             }
             ]
   });
netIncomeChart.render();
}

function httpGet(theUrl)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", theUrl, false); // false for synchronous request
    xmlHttp.send(null);
    return JSON.parse(xmlHttp.responseText);
}
