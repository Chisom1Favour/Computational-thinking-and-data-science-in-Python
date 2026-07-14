import time

class DataReport:
    def __init__(self, raw_data):
        self.raw_data = raw_data
        self._processed_data = None

    @property
    def processed_data(self):
        if self._processed_data is None:  # compute only once
            print("Processing... this takes 3 seonds")
            time.sleep(3)
            self._processed_data = sum(self.raw_data)
        return self._processed_data
    

report = DataReport([1, 2, 3, 4, 5])
print("Report created")
print(report.processed_data)
print(report.processed_data)