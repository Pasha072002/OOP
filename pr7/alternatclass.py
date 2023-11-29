import datetime

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def from_birth_year(cls, name, birth_year):
        current_year = datetime()
        age = current_year - birth_year
        return cls(name, age)

person = Person.from_birth_year("Alice",1980)
print("Name:", person.name)
print("Age:", person.age)