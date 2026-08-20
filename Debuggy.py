class Player:
    def __init__(self, health):
        self._health = health

    @property
    def health(self):
        return self._health
    @health.setter
    def health(self, value):
        print(f"Health changed: {self._health} -> {value}")
        import traceback
        traceback.print_stack()
        self._health = value

t = Player(20)
print(t.health)
t.health = 15
print(t.health)