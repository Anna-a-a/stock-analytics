function init_chart() {
const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);
const ticker = urlParams.get('ticker')

var stock = httpGet("/api/stock/" + ticker);
document.getElementById('price').innerHTML = stock.price;
document.getElementById('head-title').innerHTML = stock.name + " - " + stock.ticker;


document.getElementById('dividends-percent-average').innerHTML = stock.dividends_percent_average + "%";
document.getElementById('revenue-percent-average').innerHTML = stock.revenue_percent_average + "%";
document.getElementById('netIncome-percent-average').innerHTML = stock.net_income_percent_average + "%";


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
                 dataPoints: stock.revenueChartData.q1
             },
             {
                 type: "column",
                 indexLabel: "{y}",
                 indexLabelPlacement: "inside",
                 indexLabelOrientation: "horizontal",
                 type: "stackedColumn",
                 dataPoints: stock.revenueChartData.q2
             },
             {
                 type: "column",
                 indexLabel: "{y}",
                 indexLabelPlacement: "inside",
                 indexLabelOrientation: "horizontal",
                 type: "stackedColumn",
                 dataPoints: stock.revenueChartData.q3
             },
             {
                 type: "column",
                 indexLabel: "{y}",
                 indexLabelPlacement: "inside",
                 indexLabelOrientation: "horizontal",
                 type: "stackedColumn",
                 dataPoints: stock.revenueChartData.q4
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
                 dataPoints: stock.netIncomeChartData.q1
             },
             {
                 type: "column",
                 indexLabel: "{y}",
                 indexLabelPlacement: "inside",
                 indexLabelOrientation: "horizontal",
                 type: "stackedColumn",
                 dataPoints: stock.netIncomeChartData.q2
             },
             {
                 type: "column",
                 indexLabel: "{y}",
                 indexLabelPlacement: "inside",
                 indexLabelOrientation: "horizontal",
                 type: "stackedColumn",
                 dataPoints: stock.netIncomeChartData.q3
             },
             {
                 type: "column",
                 indexLabel: "{y}",
                 indexLabelPlacement: "inside",
                 indexLabelOrientation: "horizontal",
                 type: "stackedColumn",
                 dataPoints: stock.netIncomeChartData.q4
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
