class Vehicle:
    def __init__(self,brand):
        self.brand=brand
    def __str__(self):
        return f' vehicle brand:{self.brand}'
class Car(Vehicle):
    def __init__(self, brand,model):
        super().__init__(brand)
        self.model=model
    def __str__(self):
        return f'car brand:{super().__str__()},{self.model}'
class Bike(Vehicle):
    def __init__(self, brand,type_):
        super().__init__(brand)
        self.type_=type_
    def __str__(self):
        return f'bike brand:{super().__str__()},{self.type_}'

car=Car('toyota','corolla')
bike=Bike('yamaha','sport')
print(car)
print(bike)