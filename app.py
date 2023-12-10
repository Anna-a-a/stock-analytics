import json
import pickle

from flask import Flask, jsonify
from models.column_chart_data import ColumnChart
from models.stock import Stock
from models.stacked_column_chart_data import StackedColumnChart
from repository import getStock, getDividends , getReportDataByQ

app = Flask(__name__)


@app.route('/api/stock/<ticker>')
def stocks(ticker):
    stockDb = getStock(ticker)
    dividends = getDividends(ticker)

    q1 = getReportDataByQ(ticker, 1)
    q2 = getReportDataByQ(ticker, 2)
    q3 = getReportDataByQ(ticker, 3)
    q4 = getReportDataByQ(ticker, 4)

    stock = Stock(stockDb[1], stockDb[2], dividends, StackedColumnChart(q1, q2, q3, q4))
    return jsonify(stock.serialize())
    #return jsonify(reportData)


if __name__ == '__main__':
   app.run(port=8000, debug=True)