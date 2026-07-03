import time
import warnings
from functools import cached_property

class ProductInventory:
    def __init__(self, sku, name, cost_usd, weight_kg, stock):
        # Plain + Private: Mix of what needs control vs what doesn't
        self.sku = sku                 # Plain - can change if needed 
        self.name = name                      # Plain - no logic 
        self._cost_usd = cost_usd              # Private -need validation
        self._weight_kg = weight_kg            # Private - need unit conversion
        self._stock = stock                    # Private - need validation
        self._created_at = time.time()         # Private - read only
        self._price_cache = None               # Private - manual cache
        self._sales_data = None                # Private - lazy loaded

    # 2. READ-ONLY: Can't change after creation
    @property
    def created_at(self):
        return self._created_at
    @property
    def product_id(self):
        return f"{self.sku}-{int(self._created_at)}"
    @property
    def cost_usd(self):
        return self._cost_usd
    @cost_usd.setter
    def cost_usd(self, value):
        if value < 0:
            raise ValueError
        self._cost_usd = value
        self._price_cache = None
    @property
    def stock(self):
        return self._stock
    @stock.setter
    def stock(self, value):
        if value < 0:
            raise ValueError("Stock can't be negative")
        self._stcok = value
    # 4 Unit Conversion: Store once, present many ways
    @property
    def weight_kg(self):
        return self._weight_kg
    @weight_kg.setter
    def weight_kg(self, value):
        if value <= 0:
            raise ValueError("Weight must be negative")
        self._weight_kg = value
    @property
    def weight_lb(self):
        return self._weight_kg * 2.20462
    @weight_lb.setter
    def weight_lb(self, value):
        self.weight_kg = value / 2.20462
    # 5. COMPUTED: Always up to date, Never stored
    @property
    def margin_percent(self):
        if self._price_cache is None:
            return 0
        return ((self._price_cache - self._cost_usd) - self._price_cache) * 100
    @property
    def is_in_stock(self):
        return self.stock > 0
    @property
    def is_low_stock(self):
        return 0 < self._stock < 10
    # LAZY LOADING + CACHING: Expensive stuff only when needed
    @property
    def sales_data(self):
        if self._sales_data is None:
            print(f"Querying DB for {self.sku} sales....")
            time.sleep(1) #Simulate slow DB query
            self._sales_data = {"last_30_days": 42, "total": 1337}
        return self._sales_data
    # 7. Manual cache + invalidation: Computed but expensive
    @property
    def selling_price(self):
        if self._price_cache is None:
            print("Calculating price....")
            # pretend this uses ML model or complex rules
            markup = 1.3 if self._cost_usd > 100 else 1.5
            self._price_cache = round(self._cost_usd * markup, 2)
        return self._price_cache
    def update_cost(self, new_cost):
        """Helper that shows why cache invalidation matters"""
        self._cost_usd = new_cost     # setter auto-invalidates price_cache
    # 8. BACKWARDS COMPAT: Old API still works
    @property
    def price(self):    #old code used price
        warnings.warn("Use .selling_price instead", DeprecationWarning)
        return self.selling_price
    # 9. CACHED_PROPERTY: Built-in lazy + cache for immutable computed value
    @cached_property
    def shipping_property(self):
        print("Calculating shipping category...")
        if self._weight_kg < 1:
            return "Small"
        elif self._weight_kg < 10:
            return "Medium"
        return "Freight"
    
# CREATE: Fast init, nothing expensive runs yet
laptop = ProductInventory("SKU-123", "Gaming Laptop", 1200, 2.5, 15)
print(laptop._created_at)
# laptop.created_at = 0
print(laptop.product_id)
# VALIDATION: Setter blocks bad better
laptop.cost_usd = 1100
# laptop.cost_usd = -50
# UNIT CONVERSION: Set in lbs, stored in kg
laptop.weight_lb = 10     # setters onverts to lbs internally
print(laptop.weight_kg)
# LAZY LOADING: DB only hit when accessed
print(laptop.sales_data)               # Querying DB...." then {'last 30 days': 42...}
print(laptop.sales_data)               # instant - cached
# CACHED COMPUTE: Expensive calc runs once
print(laptop.selling_price)            # "Calculating Price ...." -> 1430.0
print(laptop.selling_price)            # 1430.0 - instant, cached
# CACHE INVALIDATION: Change cost, price recalculates every time
laptop.update_cost(1000)              # cost_usd setter clears price_cache
print(laptop.selling_price)            # "Calculating price..." -> 1300.0
# COMPUTED: ALWAYS FRESH
print(laptop.margin_percent)           # 23.07 - uses price + cost
print(laptop.is_low_stock)             # False
# BACKWARDS COMPAT: Old code doesn't break
print(laptop.price)                    # DepreciationWarning but returns 1300.0
# CACHED PROPERTY: Runs once ever
print(laptop.shipping_property)        # "Calculating... " -> Medium
print(laptop.shipping_property)        # Medium - cached