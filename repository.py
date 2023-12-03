import sqlite3

def getConnect():
   connect = sqlite3.connect('db/stock.db')
   return connect

def getStock(ticker):
    connect = getConnect()
    cur = connect.execute('SELECT * FROM stock WHERE ticker = ?', (ticker,))
    stock = cur.fetchone()
    connect.close()

    return stock

