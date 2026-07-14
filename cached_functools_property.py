from functools import cached_property

class DataSet:
    def __init__(self, numbers):
        self.numbers = numbers

    @cached_property
    def variance(self):
        print("Computing variance")
        mean = sum(self.numbers) / len(self.numbers)
        return sum((x - mean) ** 2 for x in self.numbers) / len(self.numbers)
    
d = DataSet([1, 2, 3, 4, 5])
print(d.variance)
print(d.variance)