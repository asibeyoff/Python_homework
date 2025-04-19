class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species
    
    def eat(self):
        return f"{self.name} the {self.species} is eating."
    
    def sleep(self):
        return f"{self.name} the {self.species} is sleeping."

class Cow(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Cow")
    
    def produce_milk(self):
        return f"{self.name} the {self.species} is producing milk."

class Chicken(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Chicken")
    
    def lay_egg(self):
        return f"{self.name} the {self.species} has laid an egg."

class Sheep(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Sheep")
    
    def shear_wool(self):
        return f"{self.name} the {self.species} has been sheared for wool."

# Create instances and demonstrate behaviors
def main():
    cow = Cow("Bessie", 3)
    chicken = Chicken("Clucky", 1)
    sheep = Sheep("Woolly", 2)
    
    animals = [cow, chicken, sheep]
    
    for animal in animals:
        print(animal.eat())
        print(animal.sleep())
    
    # Specific behaviors
    print(cow.produce_milk())
    print(chicken.lay_egg())
    print(sheep.shear_wool())

if __name__ == "__main__":
    main()