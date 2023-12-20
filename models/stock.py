

class Stock:
    def __init__(self, name, ticker, dividendsColumnChartData, revenueChartData, netIncomeChartData, price, dividends_percent_average, revenue_percent_average, net_income_percent_average):
        self.name = name
        self.ticker = ticker
        self.dividendsColumnChartData = dividendsColumnChartData
        self.revenueChartData = revenueChartData
        self.netIncomeChartData = netIncomeChartData
        self.price = price
        self.dividends_percent_average = dividends_percent_average
        self.revenue_percent_average = revenue_percent_average
        self.net_income_percent_average = net_income_percent_average


    def serialize(self):
        return {
            'name': self.name,
            'ticker': self.ticker,
            'dividendsColumnChartData': [item.serialize() for item in self.dividendsColumnChartData],
            'revenueChartData': self.revenueChartData.serialize(),
            'netIncomeChartData': self.netIncomeChartData.serialize(),
            'price': self.price,
            'dividends_percent_average': self.dividends_percent_average,
            'revenue_percent_average': self.revenue_percent_average,
            'net_income_percent_average': self.net_income_percent_average
        }

