class TradeData:
    def __init__(self, df):
        self._df = df

    @property
    def revenue(self):
        return self._df["price"] * self._df["quantity"]
    
    @property
    def profit(self):
        return self.revenue - self._df["cost"]
    
    @property
    def profit_margin(self):
        return self.profit /self.revenue
    

data = TradeData(df)
df["quantity"] = 200
print(data.profit)