class Weather:
    def __init__(self, celsius):
        self._celsius = celsius
    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32
    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5/9

w = Weather(30)
print(w.fahrenheit)
w.fahrenheit = 32