class Room:
    length = 0.0
    width = 0.0

    # Метод обчислення площі
    def calculate_area(self):
        print("Area of Room =", self.length * self.width)

study_room = Room()

study_room.length = 42.5
study_room.width = 30.8

# Отримання доступ до методу всередині класу
study_room.calculate_area()