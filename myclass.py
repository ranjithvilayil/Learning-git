class Person:
    def __init__(self, name, location, native):
        self.name = name
        self.location = location
        self.native = native
        self.items = []
        
    def sing(self):
        return f"{self.name} is singing &&"
        
    def walk(self):
        return f"{self.name} is walking - Tak Tak Tak"
    
    def speak(self):
        return f"{self.name} speaking!"