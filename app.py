from flask import Flask, jsonify
import sqlite3
from src.models.column_chart_data import ColumnChart
from src.models.stock import Stock

app = Flask(__name__)

def get_db():
   db = sqlite3.connect('utils/db_functions/stock.db')
   return db

def create_chart(label, y):
    chart = ColumnChart(label, y)
    return chart

@app.route('/api/stock/<ticker>')
def stocks(ticker):
    db = get_db()
    cur = db.execute('SELECT name FROM stock WHERE ticker = ?', (ticker,))
    stock_name = cur.fetchone()[0]
    list_of_charts = [create_chart("2023", 1.1), create_chart("2023", 1.17)]

    stock = Stock(stock_name, ticker, list_of_charts)
    return jsonify(stock.serialize())


if __name__ == '__main__':
   app.run(debug=True)