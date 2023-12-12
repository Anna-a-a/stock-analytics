

class Stock:
    def __init__(self, name, ticker, dividendsColumnChartData, revenueChartData, netIncomChartData):
        self.name = name
        self.ticker = ticker
        self.dividendsColumnChartData = dividendsColumnChartData
        self.revenueChartData = revenueChartData
        self.netIncomChartData = netIncomChartData

    def serialize(self):
        return {
            'name': self.name,
            'ticker': self.ticker,
            'dividendsColumnChartData': [item.serialize() for item in self.dividendsColumnChartData],
            'revenueChartData': self.revenueChartData.serialize(),
            'netIncomChartData': self.netIncomChartData.serialize()
        }

