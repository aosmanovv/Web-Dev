from models.Animal import Animal

class Cat(Animal):
    def __init__(self, name, age, color, favorite_toy):
        super().__init__(name, age, color)
        self.favorite_toy = favorite_toy

    def speak(self):
        return "Meow"

    def play(self):
        return f"{self.name} is playing with {self.favorite_toy}"