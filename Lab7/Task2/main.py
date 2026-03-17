from models.Animal import Animal
from models.Dog import Dog
from models.Cat import Cat

def main():
    animals = [
        Dog("Zim", 2, "black", "Sobachka"),
        Cat("Shasya", 14, "grey", "Poprigunchik"),
        Dog("Humcha", 15, "brown", "Starushka"),
        Cat("Bagira", 7, "black", "laser pointer")
    ]

    for pet in animals:
        print(pet)
        print(pet.describe())
        print("Sound:", pet.speak())

        if isinstance(pet, Dog):
            print("Dog action:", pet.wag_tail())
        elif isinstance(pet, Cat):
            print("Cat action:", pet.play())


if __name__ == "__main__":
    main()