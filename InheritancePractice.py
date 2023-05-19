class human():
    def __init__(self, human_gender = "unknown", age = 0):
        self.human_gender = human_gender
        self.age = age
    def speak(self):
            print("Hi, i am human and i have no gender")

class man(human):   #sub class of man
    def __init__(self,):
        super().__init__(human_gender = "Male")  # overides original gender from super class
    def speak(self):
            print("Hi, i am human and my gender is: ", self.human_gender)

class AttackHelicopter(human):
    def __init__(self,):
        super().__init__(human_gender = "Machine")
    def speak(self):
         print("*Blades spin intensly*")
          

A_man = man()
print("The human is a ", A_man.human_gender)
print("The human is: ", A_man.age)
A_man.speak()
print(" ")


A_helicopter = AttackHelicopter()
print("The human is a ", A_helicopter.human_gender)
print("The human is: ", A_helicopter.age)
A_helicopter.speak()