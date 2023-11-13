#1 write abstract class Animal
class Animal:
    def __init__(self, name, age):
        # share private attributes name, age
        self.name = name
        self.age = age
    # abstract method speak()
    def speak(self):
        pass
    # method to display age of animal instance    
    def display_age(self):
        print(f"{self.name} is {self.age} years old.")

# implementation Cat 
class Cat(Animal):
         # abstract method speak() prints behavior
        def speak(self):
            print(f"{self.name} the Cat says Meow!")

# implementation Dog
class Dog(Animal):
         # abstract method speak() prints behavior
        def speak(self):
            print(f"{self.name} the Dog says Woof!")

#2 implement class Zoo 
class Zoo:
    def __init__(self):
        self.animals = []

#a attribute list of animal objects
    def add_animal(self, animal):
        self.animals.append(animal)

#b calls speak method for each animal in the current instance
    def speak_all(self):
        for animal in self.animals:
            animal.speak()

#3 implement class Zookeeper
class ZooKeeper:
    # attribute: single Zoo instance
    def __init__ (self, name):
        self.name = name
        self.zoo = Zoo()

    # method: add_animal(animal : Animal)
    def add_animal(self, animal):
        self.zoo.add_animal(animal)
        print (f"{self.name} adds {animal.name} to the zoo.")
         

