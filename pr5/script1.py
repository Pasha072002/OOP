class Car:
    def __init__(self, brand, model):
        self.brand = brand  # Змінна класу
        self.model = model  # Змінна класу

    def get_brand(self):
        return self.brand

    def set_model(self, new_model):
        self.model = new_model


my_car = Car("Toyota", "Corolla")


print(my_car.brand)  
print(my_car.model)  

my_car.set_model("Camry")
print(my_car.model)  