from vetClasses import *

#Object instantiation 
Allie = Cat("Allie", 10, "White", "Shorthair")

#newname = input("Please enter the cats name: ")
#cat1.name = newname

Rex = Dog("Rex", 7, "Red", "Golden Retriever")
print(Rex.grow())
print(Rex.die())

Goldie = AFish("Goldie", 12, "Yellow", "Clownfish", "Pacific Ocean")
print(Goldie.move())
print(Goldie.eat())
print(f"{Goldie.breed} live in the {Goldie.location}")
print(Goldie.jump())

Birdie = ABird("Birdie", 12, "Yellow", "Spotted Finch", "7cm", "Arkansas")
print(Birdie.grow())
print(Birdie.name)
print(Birdie.eat())

MrPaws = Cat("MrPaws", 3, "Black", "Persian")

animal_list = [Allie, Rex, Goldie, Birdie, MrPaws]



