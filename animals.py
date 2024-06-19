
#   def eat(self):
#       print(f"{self.name} is eating")

#   def __str__(self):
#       return f"{self.name} - {self.species} - {self.__class__.__name__}"

# class Cat(Animal):
#   def __init__(self, name, species, breed):
#       super().__init__(name, species)
#       self.breed = breed

#   def meow(self):
#       print("meow")

#   def __str__(self):
#       return super().__str__() + f"- {self.breed}"

# my_cat = Cat("w", "x", "y")

# my_cat.eat()
# my_cat.meow()

# print(my_cat)

class Bird:
   def __init__(self, name, species):
     self.name = name
     self.species = species

class Owl(Bird):
    def __init__(self, name, species, colour):
      super().__init__(name, species)
      self.colour = colour


class Dodo(Bird):
    def __init__(self, name, species, colour):
      super().__init__(name, species)
      self.colour = colour

bird1 = Owl("Devi", "Owl", "Blue")
bird2 = Dodo("Owlie", "Dodo", "Red")

print(bird1.name, bird1.species, bird1.colour)
print(bird2.name, bird2.species, bird2.colour)
  