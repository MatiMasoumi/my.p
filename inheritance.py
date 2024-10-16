class Animal:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return f'animal name:{self.name}'
class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed=breed
    def __str__(self):
        return f'{super().__str__()},{self.breed}'
    
