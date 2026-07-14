"""Use because internal representation might change later"""

class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius
    
    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32
    
    @property
    def kelvin(self):
        return self._celsius + 273.15
    
t = Temperature(13)
print(t.fahrenheit)
print(t.kelvin)