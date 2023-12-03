from flask import Flask, jsonify
from models.column_chart_data import ColumnChart
from models.stock import Stock
from repository import getStock

app = Flask(__name__)



@app.route('/api/stock/<ticker>')
def stocks(ticker):
    list_of_charts = [ColumnChart("2023", 1.1), ColumnChart("2023", 1.17)]

    stockDb = getStock(ticker)
    stock = Stock(stockDb[1], stockDb[2], list_of_charts)
    return jsonify(stock.serialize())


if __name__ == '__main__':
   app.run(port=8000, debug=True)