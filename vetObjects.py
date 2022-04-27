from vetClasses import *

#Object instantiation 
Allie = Cat("Allie", 10, "White")
print(Allie.eat())
#newname = input("Please enter the cats name: ")
#cat1.name = newname

Rex = Dog("Rex", 7, "Red")
print(Rex.grow())
print(Rex.die())

Goldie = AFish("Goldie", "Goldfish", "Golden", "Pacific Ocean")
print(Goldie.move())
print(Goldie.eat())
print(f"{Goldie.type} live in the {Goldie.region}")
print(Goldie.jump())

Birdie = ABird("7cm", "Arkansas", "Yellow", "Spotted Finch", "Birdie")
print(Birdie.grow())
print(Birdie.name)
print(Birdie.eat())

animal_list = [Allie, Rex, Goldie, Birdie]
for id, animal in enumerate(animal_list):
    print(id)
    print(animal)

