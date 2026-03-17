class Animal:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def speak(self):
        return "Some generic animal sound..."

    def describe(self):
        return f"{self.name} is {self.age} years old and has {self.color} color"

    def __str__(self):
        return f"{self.__class__.__name__}: {self.name}, {self.age} years, {self.color}"
