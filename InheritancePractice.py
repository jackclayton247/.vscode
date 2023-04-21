class human():
    def __init__(self, human_gender = "unknown", age = 0):
        self.human_gender = human_gender
        self.age = age
    
class man(human):
    def __init__(self,):
        super().__init__(human_gender = "Male")
    def speak(self):
            print("Hi, i am human and my gender is: ", self.human_gender)
            
A_man = man()
print("The human is a ", A_man.human_gender)
print("The human is: ", A_man.age)
A_man.speak()