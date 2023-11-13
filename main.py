# main.py
from animals import Animal, Cat, Dog, Zoo, ZooKeeper

if __name__ == "__main__":
    # create animal objects
    cat = Cat("Whiskers", 5)
    dog = Dog("Buddy", 3)
    
    # create animal age objects for print statement
    cat.display_age()
    dog.display_age()

    # Create a Zoo and add animals
    zoo = Zoo()
    zoo.add_animal(cat)
    zoo.add_animal(dog)

    # Create a ZooKeeper and add animals to the zoo
    zookeeper = ZooKeeper("John")
    zookeeper.add_animal(cat)
    zookeeper.add_animal(dog)

    # Have the zookeeper make the animals speak
    zookeeper.zoo.speak_all()
