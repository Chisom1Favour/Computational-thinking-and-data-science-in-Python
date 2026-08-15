import time

class DataReport:
    def __init__(self, raw_data):
        self.raw_data = raw_data
        self._processed_data = None

    @property
    def processed_data(self):
        if self._processed_data is None:
            print("Processing time")
            time.sleep(3)
            self._processed_data = sum(self.raw_data)
        return self._processed_data
    
data = DataReport([1, 2, 3, 4, 5])
print(data.processed_data)
print(data.processed_data)
