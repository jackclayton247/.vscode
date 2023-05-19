

#sets the human class
class human():
    def __init__(self, name = "no name", age = 0, nationality = "no nationality", gender = "no gender", hobby = "no hobby", FootSize = "no feet"):

        self.name = name
        self.age = age
        self.nationality = nationality
        self.gender = gender
    def speak(self):
        print("hello")
    def joke(self):
        print("What do you call a lazy kangaroo? \n A pouch potato")

Greg = human()
Greg.name, Greg.age, Greg.nationality, Greg.gender = "Greg", 87, "Bri'ish (Brexit Geeza)", "Male"
print("Object's Attributes:")
print("********************")
print("")
print(Greg.name)
print(Greg.age)
print(Greg.nationality)
print(Greg.gender)
print("")
print("Objects's Methods:")
print("********************")
Greg.joke()

Rees = human()
Rees.name, Rees.age, Rees.nationality, Rees.gender, Rees.hobby, Rees.FootSize = "Reece", "13", "Stupid", "Unknown", "Poopy Head", "Size 4 Dunks"
print("Object's Attributes:")
print("********************")
print("")
print("Name:",Rees.name)
print("Age:",Rees.age)
print("Nationality:",Rees.nationality)
print("Gender:",Rees.gender)
print("Hobby:",Rees.hobby)
print("Foot Size:",Rees.FootSize)
print("")
print("Objects's Methods:")
print("********************")