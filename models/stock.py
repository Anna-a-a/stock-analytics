class Stock:
    def __init__(self, name, ticker, dividendsColumnChartData):
        self.name = name
        self.ticker = ticker
        self.dividendsColumnChartData = dividendsColumnChartData

    def serialize(self):
        return {
            'name': self.name,
            'ticker': self.ticker,
            'dividendsColumnChartData': [item.serialize() for item in self.dividendsColumnChartData]
        }

