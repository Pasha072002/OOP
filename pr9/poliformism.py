class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Person: {self.name}"

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other_point):
        return Point(self.x + other_point.x, self.y + other_point.y)

class Fruit:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other_fruit):
        return self.name == other_fruit.name

# Використання "магічних методів"
person = Person("Alice")
print(person)  

point1 = Point(1, 2)
point2 = Point(3, 4)
result = point1 + point2
print(result.x, result.y)  

apple1 = Fruit("Apple")
apple2 = Fruit("Apple")
banana = Fruit("Banana")

print(apple1 == apple2)  
print(apple1 == banana)  