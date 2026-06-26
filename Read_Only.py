import time
class File:
    def __init__(self, name):
       self.name = name
       self._created_at = time.time()

    @property
    def created_at(self): # No setter, read-only
        return self._created_at
    
f = File("File.pdf")
f.created_at = 0