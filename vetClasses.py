#Implement animal class-based hierarchy
#Attributes are only defined in concrete classes

from abc import ABC, abstractmethod

#Class definitions
class Animal(ABC):
    #Constructor
    value = "Animal"
    def __init__(self, name, age, color, breed):
        self.name = name
        self.age = age
        self.color = color
        self.breed = breed

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
    value = "Bird"
    def __init__(self, name, age, color, breed, wingspan, location):
        super().__init__(name, age, color, breed)
        self.wingspan = wingspan
        self.location = location

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
    value = "Mammal"
    def __init__(self, name, age, color, breed):
        super().__init__(name, age, color, breed)

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
    value = "Fish"
    def __init__(self, name, age, color, breed, location):
        super().__init__(name, age, color, breed)
        self.location = location

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
    value = "Cat"
    def __init__(self, name, age, color, breed):
        super().__init__(name, age, color, breed)

    #Methods
    def __str__(self):
        return f"{self.name}: A {self.value}"

    def type(self):
        return(self.value)

    def eat(self):
        return(f"{self.name} eats mice")

class Dog(Mammal):
    #Constructor
    value = "Dog"
    def __init__(self, name, age, color, breed):
        super().__init__(name, age, color, breed)

    #Methods
    def __str__(self):
        return f"{self.name}: A {self.value}"

    def type(self):
        return(self.value)

    def eat(self):
        return("I eat dog food")

class AFish(Fish):
    #Constructor
    value = "Fish"
    def __init__(self, name, age, color, breed, location):
        super().__init__(name, age, color, breed, location)

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
    value = "Bird"
    def __init__(self, name, age, color, breed, wingspan, location):
        super().__init__(name, age, color, breed, wingspan, location)

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


