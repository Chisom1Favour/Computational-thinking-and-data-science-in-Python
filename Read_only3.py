import time

class File:
    def __init__(self, name):
        self.name = name
        self._created_at = time.time()
    @property
    def created_at(self):
        return self._created_at


f = File("Chinaza")
f.created_at = 0