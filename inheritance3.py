class Animal:
    def __init__(self,name):
        self.name=name
    def sound(self):
        return 'some animal sound'
    def __str__(self):
        return f'animal name:{self.name}'
class Bird(Animal):
    def __init__(self, name,fly):
        super().__init__(name)
        self.fly=fly
    def sound(self):
        return 'chrip chrip'
    def __str__(self):
        return f'{super().__str__()},{self.fly}'
class Sparrow(Bird):
    def __init__(self, name, fly,wingspan):
        super().__init__(name, fly)
        self.wingspan=wingspan
    def __str__(self):
        return f'{super().__str__()},{self.wingspan}'
    
    
sp=Sparrow('jack',True,20)
print(sp)
print(sp.__dict__)
print(sp.sound())