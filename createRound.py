class Round:

    def __init__(self, briwer):
        self.name = briwer
        self.order = {}

    def add_order(self, name, drink):
        self.order[name] = drink


danny_round = Round("Danny")
danny_round.add_order("John", "Milk")

henry_round = Round("Henry")
henry_round.add_order("David", "Water")

print(danny_round.order)
print(henry_round.order)

class Drink:

    def __init__(self, drink_name, drink_type, temperature, available):
        self.name = drink_name
        self.type = drink_type
        self.temp = temperature
        self.available = available
    
    def is_hot(self):
        self.temp = "Hot"

    def is_cold(self):
        self.temp = "Cold"

    def is_available(self):
        self.available = "Yes"

class Hot_drink(Drink):

    pass

class Person:

    def __init__(self, person_name, team, fave_drink):
        self.name = person_name
        self.team = team
        self.drink = fave_drink

#Person (Name, Team, Favourite Drink etc)
#Drink (Name, Type, Temperature etc)