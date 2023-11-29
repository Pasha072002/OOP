class TemperatureConverter:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5/9

# Створення об'єкту класу TemperatureConverter
temp = TemperatureConverter(25)

# Виведення температури в Цельсіях та Фаренгейтах
print(temp.celsius)     
print(temp.fahrenheit) 

# Зміна температури у Фаренгейтах та перегляд у Цельсіях
temp.fahrenheit = 32
print(temp.celsius)     
print(temp.fahrenheit)  
