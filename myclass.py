class Person:
    def __init__(self, name, location, native):
        self.name = name
        self.location = location
        self.native = native
        self.items = []
        
    def sing(self):
        return f"{self.name} is singing &&"
        