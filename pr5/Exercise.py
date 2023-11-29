# У нас є клас, визначений для транспортних засобів. Створіть два нових транспортних засобу під назвою car1 і car2. 
# Встановіть, що car1 буде червоним кабріолетом вартістю $60 000,00 на ім’я Fer, а car2 — синім фургоном під назвою Jump вартістю $10 000,00.

class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

# your code goes here
car1 = Vehicle()
car1.name = "Fer"
car1.color = "Red"
car1.value = 60000.00
car1.kind = "convertible"

car2 = Vehicle()
car2.name = "Jump"
car2.color = "blue"
car2.kind = "van"
car2.value = 10000.00

print(car1.description())
print(car2.description())