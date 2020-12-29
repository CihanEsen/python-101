class Person:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def bmi(self):
        total = self.weight / self.height ** 2
        return total
