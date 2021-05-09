class Car:
    maker = ""
    model = ""
    weight = 2000

    def __init__(self, **kwargs):
        self.maker = kwargs["maker"]
        self.model = kwargs["model"]

    def add(self, kg):
        self.weight += kg

    def __str__(self):
        return self.maker

class MersedesBenz(Car):
    pass



lada = Car(model="Kalina", maker="Lada")
print(lada.weight)
lada.add(30)
print(lada.weight)
print(lada.maker)

m = MersedesBenz(model="S600", maker="Mersedes")
