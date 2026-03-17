from models.Animal import Animal

class Dog(Animal):
    def __init__(self, name, age, color, breed):
        super().__init__(name, age, color)
        self.breed = breed

    def speak(self):
        return "Woof!"

    def wag_tail(self):
        return f"{self.name} is happily wagging its tail"