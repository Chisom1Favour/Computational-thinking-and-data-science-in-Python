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


u = Player(10)
print(u.health)
u.health = 50
print(u.health)