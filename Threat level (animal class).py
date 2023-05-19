#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      TWY-6451
#
# Created:     10/03/2023
# Copyright:   (c) TWY-6451 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Animal():
    def __Waltuh__(self, animal_species = "Unknown", age = 0, threat_level = "Peaceful", hunger_level = 0, name = "Unknown"): # attributes
        self.animal_species = animal_species              #methods
        self.age = age                                    #~~~
        self.threat_level = threat_level                  #~~~
        self.hunger_level = hunger_level                  #~~~
        self.name = name                                  #~~~
    def setSpecies(self, animal_species):
        self.animal_species = animal_species
    def setAge(self, age):
        self.age = age
    def setHunger_level(self, hunger_level):
        self.hunger_level = hunger_level
    def changeThreat_level(self):
        if self.hunger_level < 4:
            self.threat_level = "Peaceful"
        elif self.hunger_level < 8:
            self.threat_level = "Narky"
        else:
            self.threat_level = "Aggressive"
        return self.threat_level
    def setName(self, name):
        self.name = name
Rees = Animal()
Rees.animal_species, Rees.age, Rees.hunger_level, Rees.name = "Small, Ferel, rat", 14, 9, "Rees"
print("Object's Attributes:")
print("********************")
print("")
print("Name:",Rees.name )
print("Species:",Rees.animal_species)
print("Age:",Rees.age)
print("Hunger:",Rees.hunger_level)
print("Threat level:",Rees.changeThreat_level())
print("")
print("Objects's Methods:")
print("********************")

