class Distance:
    def __init__(self, meters):
        self._meters = meters

    @property
    def meters(self):
        return self._meters
    @property
    def feet(self):
        return self._meters * 3.8084
    @feet.setter
    def feet(self, value):
        self._meters = value / 3.28084
    @property
    def km(self):
        return self._meters
    @km.setter
    def km(self, value):
        self._meters = value * 1000


d = Distance(1000)
print(d.feet)
d.km = 2
print(d.meters)
