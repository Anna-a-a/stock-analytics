import sqlite3

from models.column_chart_data import ColumnChart


def getConnect():
    connect = sqlite3.connect('db/stock.db')
    return connect


def getStock(ticker):
    connect = getConnect()
    cur = connect.execute('SELECT * FROM stock WHERE ticker = ?', (ticker,))
    result = cur.fetchone()
    connect.close()

    return result


def getDividends(ticker):
    connect = getConnect()
    cur = connect.execute(
        'SELECT * FROM dividends INNER JOIN Stock ON dividends.stock_id = Stock.Stock_id WHERE ticker = ?', (ticker,))

    dividendsDb = cur.fetchall()
    list_of_charts = []
    for i in dividendsDb:
        list_of_charts.append(ColumnChart(i[1], i[2]))

    connect.close()
    return list_of_charts


def getReportDataByQ(ticker, q):
    connect = getConnect()
    cur = connect.execute(
        'SELECT year, revenue FROM report_data INNER JOIN Stock ON report_data.stock_id = stock.Stock_id WHERE ticker = ? AND q = ?', (ticker, q))

    result = cur.fetchall()
    reportData = []
    for i in range(len(result)):
        reportData.append(ColumnChart(result[i][0], result[i][1]))

    connect.close()
    return reportData