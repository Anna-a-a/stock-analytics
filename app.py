from flask import Flask, jsonify

from models.stacked_column_chart_data import StackedColumnChart
from models.stock import Stock
from repository import getStock, getDividends, getRevenueByQ, getNetIncomeByQ

app = Flask(__name__)


@app.route('/api/stock/<ticker>')
def stocks(ticker):
    stockDb = getStock(ticker)
    dividends = getDividends(ticker)

    revenueQ1 = getRevenueByQ(ticker, 1)
    revenueQ2 = getRevenueByQ(ticker, 2)
    revenueQ3 = getRevenueByQ(ticker, 3)
    revenueQ4 = getRevenueByQ(ticker, 4)

    netIncomQ1 = getNetIncomeByQ(ticker, 1)
    netIncomQ2 = getNetIncomeByQ(ticker, 2)
    netIncomQ3 = getNetIncomeByQ(ticker, 3)
    netIncomQ4 = getNetIncomeByQ(ticker, 4)



    stock = Stock(stockDb[1], stockDb[2], dividends, StackedColumnChart(revenueQ1, revenueQ2, revenueQ3, revenueQ4),
                  StackedColumnChart(netIncomQ1, netIncomQ2, netIncomQ3, netIncomQ4))
    return jsonify(stock.serialize())
    #return jsonify(reportData)


if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8000)