class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name}."

    def increase_age(self, years):
        self.age += years
        return f"My age is now {self.age}."


person1 = Person("Alice", 25)

print(person1.greet())  
print(person1.increase_age(5))  
