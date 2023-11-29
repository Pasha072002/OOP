# Батьківський клас
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"


# Дочірній клас, що успадковує властивості та методи від батьківського класу
class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)  # Виклик конструктора батьківського класу
        self.salary = salary

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"


class Student(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age)  # Виклик конструктора батьківського класу
        self.major = major

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, Major: {self.major}"


# Створення об'єктів дочірніх класів
employee = Employee("John", 30, 50000)
student = Student("Alice", 20, "Computer Science")

# Виведення інформації про об'єкти
print(employee.display_info())  # Виведе: Name: John, Age: 30, Salary: 50000
print(student.display_info())   # Виведе: Name: Alice, Age: 20, Major: Computer Science






