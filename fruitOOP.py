class fruit():
    def __init__(self, colour = "unknown", size = "Unknown", taste = "unknown"):
        self.colour = colour
        self.size = size
        self.taste = taste

class tropical(fruit):
    def __init__(self,):
        super().__init__(taste = "Sweet")

Mango = tropical()
print("*******************")
print("colour:", Mango.size)
print("size:", Mango.size)
print("taste:", Mango.taste)
print("*******************")
