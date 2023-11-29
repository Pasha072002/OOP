class Bike:
    name = ""
    gear = 0

bike1 = Bike() #Об'єкт класу

bike1.gear = 11 # Отримання доступу до атрибутів та присвоюємо нові значення
bike1.name = "Mountain Bike"

print(f"Name: {bike1.name}, Gears: {bike1.gear}") #Виведення дані на екран

