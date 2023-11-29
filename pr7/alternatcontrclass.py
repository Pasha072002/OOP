class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        current_year = 2023  
        age = current_year - birth_year
        return cls(name, age)


person_from_birth_year = Person.from_birth_year("Alice", 1990)

print(person_from_birth_year.name)  
print(person_from_birth_year.age)