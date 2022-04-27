#Implement animal class-based hierarchy
#Attributes are only defined in concrete classes

from abc import ABC, abstractmethod
from unicodedata import name

#Class definitions
class Animal(ABC):
    #Constructor
    def __init__(self):
        self.value = "Animal"

    #Methods
    @abstractmethod
    def reproduce(self):
        pass

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def move(self):
        pass

    def sleep(self):
        return(f"{self.name} is sleeping")

    def grow(self):
        return(f"{self.name} is growing larger")

    def die(self):
        return(f"{self.name} is dying :(")

    def type(self):
        print(self.value)

class Bird(Animal):
    #Constructor
    def __init__(self, wingspan, location, color, type, name):
        self.value = "Bird"
        self.wingspan = wingspan
        self.location = location
        self.color = color
        self.type = type
        self.name = name

    #Methods
    def eat(self):
        return(f"{self.value} eats worms")

    def move(self):
        return("I fly")
    
    def reproduce(self):
        return("I lay eggs")

    def type(self):
        return(self.value)

class Mammal(Animal):
    #Constructor
    def __init__(self):
        self.value = "Mammal"

    #Methods
    @abstractmethod
    def eat(self):
        pass

    def move(self):
        return("I move on my 4 legs")
    
    def reproduce(self):
        return("I give birth")

    def type(self):
        return(self.value)

class Fish(Animal):
    #Constructor
    def __init__(self):
        self.value = "Mammal"

    #Methods
    @abstractmethod
    def eat(self):
        pass

    def move(self):
        return(f"{self.value} swim in the water")
    
    def reproduce(self):
        return("I lay eggs")

    def type(self):
        return(self.value)

class Cat(Mammal):
    #Constructor
    def __init__(self, name, age, color):
        self.value = "Cat"
        self.name = name
        self.age = age
        self.color = color

    #Methods
    def __str__(self):
        return f"{self.name}: A {self.value}"

    def type(self):
        return(self.value)

    def eat(self):
        return(f"{self.name} eats mice")



class Dog(Mammal):
    #Constructor
    def __init__(self, name, age, color):
        self.value = "Dog"
        self.name = name
        self.age = age
        self.color = color

    #Methods
    def __str__(self):
        return f"{self.name}: A {self.value}"

    def type(self):
        return(self.value)

    def eat(self):
        return("I eat dog food")

class AFish(Fish):
    #Constructor
    def __init__(self, name, type, color, region):
        self.value = "Fish"
        self.name = name
        self.type = type
        self.color = color
        self.region = region

    #Methods
    def __str__(self):
        return f"{self.name}: A {self.value}"

    def type(self):
        return(self.value)

    def eat(self):
        return(f"{self.type} eat algae")

    def jump(self):
        return(f"{self.type} jump out of the sea and dive back in!")

class ABird(Bird):
    #Constructor
    def __init__(self, wingspan, location, color, type, name):
        super(ABird, self).__init__(wingspan, location, color, type, name)

    #Methods
    def __str__(self):
        return f"{self.name}: A {self.value}"
        
    def eat(self):
        return(f"{self.name} eats worms")

    def move(self):
        return("I fly")
    
    def reproduce(self):
        return("I lay eggs")

    def type(self):
        return(self.value)


