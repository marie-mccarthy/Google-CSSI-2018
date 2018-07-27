import math
import datetime as dt

print(dt.date.today())

petey = {
    "name": "Petey",
    "animal": "dog",
    "species": "corgi",
    "age": 9,               #oxford comma
}

fezzik = {
    "name": "fezzik",
    "animal": "giant",
    "species": "huge",
    "age": 30,
}
class Pet(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungry = True
        self.mood = "happy"

    def eat(self):
        if self.is_hungry:
            self.mood = "happy"
            self.is_hungry = False
        else:
            self.mood = "Bloated"

    def year_born(self):
        today = dt.date.today()
        year = today.year
        return year - self.age

    def play(self):
        if self.mood == "excited":
            self.mood = "tired"
            self.is_hungry = True
        else:
            self.mood = "excited"
            self.is_hungry = True

    def play_with(self, other_pet):
        self.play()
        other_pet.play()

    def __str__(self):
        return self.name + " is " +str(self.age) +"years old"

wesley = Pet("Wesley", 25)

print("My pet name is %s and age is %s" %
(wesley.name, wesley.age))
print("my pet was born in " + str(wesley.year_born()))

buttercup = Pet("Buttercup", 72)
print("Buttercup was born in "+ str(buttercup.year_born()))

fido = Pet("fido", 4)
petey = Pet("petey", 7)

#    str(buttercup.year_born()))


fido.play_with(petey)
print(petey.mood)
print(fido.mood)

fido.play_with(petey)
print(petey.mood)
print(fido.mood)
print(__str__())
"""
print("is  buttercup Hungry "+ str(buttercup.is_hungry))
wesley.eat()
print("is wesley Hungry "+ str(wesley.is_hungry))
wesley.eat()
print(wesley.mood)
wesley.play()
print(wesley.mood)
wesley.play()
print(wesley.mood)
print("is wesley Hungry "+ str(wesley.is_hungry))
print(wesley.mood)
"""
