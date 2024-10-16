class Flower:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def __str__(self):
        return f'{self.name},{self.color}'
    def show_name(self):
        print(f'Flower name:{self.name}')
class Tree:
    def __init__(self,species):
        self.species=species
    def __str__(self):
        return f'{self.species}'
    def show_name(self):
        print(f'Tree name:{self.name}')
class Plant(Tree,Flower):
    def __init__(self,name,color,species,height):
        super().__init__(species)
        Flower.__init__(self,name,color)
        self.height=height
    def __str__(self):
        return f'{super().__str__()},{Flower.__str__(self)},{self.height}'

t1=Plant('h','red','n',110)
print(t1.__dict__)
print(t1)
t1.show_name()
