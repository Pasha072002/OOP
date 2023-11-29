class Vehicle:
    def drive(self):
        return "Driving vehicle"

class Car(Vehicle):
    def drive(self):
        # Перевизначення методу
        return "Driving car"

    def drive_with_parent(self):
        # Виклик методу батьківського класу для додаткового функціоналу
        return super().drive() + " while parent is driving"

# Створення об'єктів
vehicle = Vehicle()
car = Car()

# Виклик методів
print(vehicle.drive())  
print(car.drive())      
print(car.drive_with_parent()) 