class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        pass  # Цей метод буде перевизначений у дочірніх класах


class Dog(Animal):
    def make_sound(self):
        return "Woof!"


class Cat(Animal):
    def make_sound(self):
        return "Meow!"


class PetOwner:
    def __init__(self, pet):
        self.pet = pet

    def pet_sound(self):
        if isinstance(self.pet, Animal):  # Перевірка чи pet є екземпляром класу Animal
            return self.pet.make_sound()
        else:
            return "This is not a valid pet."


# Створення об'єктів класів Dog, Cat та PetOwner
dog = Dog("Canine")
cat = Cat("Feline")

owner1 = PetOwner(dog)
owner2 = PetOwner(cat)

# Виклик методу, який використовує методи представників класу Animal
print(owner1.pet_sound())  # Виведе: Woof!
print(owner2.pet_sound())  # Виведе: Meow!