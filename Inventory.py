import time
import warnings
from functools import cached_property

class ProductInventory:
    def __init__(self, name, sku, weight_kg, cost_usd, stock):
        self.name = name
        self.sku = sku
        self._weight_kg = weight_kg
        self._cost_usd = cost_usd
        self._stock = stock
        self._created_at = time.time()
        self._price_cache = None
        self._sales_data = None

    @property
    def created_at(self):
        return self._created_at
    @property
    def product_id(self):
        return f"{self.sku} - {int(self._created_at)}"
    @property
    def cost_usd(self):
        return self._cost_usd
    @cost_usd.setter
    def cost_usd(self, value):
        if value < 0:
            raise ValueError("Cost can't be negative")
        self._cost_usd = value
        self._price_cache = None
    @property
    def stock(self):
        return self._stock
    @stock.setter
    def stock(self, value):
        if value < 0:
            raise ValueError("Stock can't be negative")
        self._stock = value
    @property
    def weight_kg(self):
        return self._weight_kg
    @weight_kg.setter
    def weight_kg(self, value):
        if value < 0:
            raise ValueError("Weight cannot be negative")
        weight_kg = value
    @property
    def weight_lb(self):
        return self._weight_kg * 2.20462
    @weight_lb.setter
    def weight_lb(self, value):
        self.weight_kg = value / 2.20462
    @property
    def margin_percent(self):
        if self._price_cache is None:
            print(f"Querying DB for {self.sku} sales...")
            time.sleep(1)
            self._sales_data = {"last 30 days": 42, "total": 1337}
        return self._sales_data
    @property
    def selling_price(self):
        if self._price_cache is None:
            print("Calculating price...")
            markup = 1.3 if self._cost_usd > 100 else 1.5
            self._price_cache = round(self._cost_usd * markup, 2)
        return self._price_cache
    def update_cost(self, new_cost):
        self._cost_usd = new_cost
    @property
    def price(self):
        warnings.warn("Use .selling_pice instead", DeprecationWarning)
        return self._selling_price
    @cached_property
    def shipping_category(self):
        if self.weight_kg < 1:
            return "Small"
        elif self.weight_kg < 10:
            return "Medium"
        return "Freight"      

laptop = ("GAMING LAPTOP", "sku-123", 25, 50, 15)
print(laptop.created_at)
print(laptop.product_id)
laptop.cost_usd = 1100
laptop.weight_lb
print(laptop.sales_data)
print(laptop.sales_data)
print(laptop.selling_price)
print(laptop.selling_price)
laptop.update_cost(1000)
print(laptop.selling_price)
print(laptop.margin_percent)
print(laptop.price)
print(laptop.shipping_category)
print(laptop.shipping_category)
