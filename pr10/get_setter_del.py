class TemperatureConverter:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def tempetarute(self):
        return self._celsius
    
    @tempetarute.setter
    def temperature(self, value):
        if value < -273.15: # Абсолютний нуль в Кельвінах (-273.15 °C)
            raise ValueError('Температура нижче абсолютного нуля неможлива')
        self._celsius = value
    
    @temperature.deleter
    def temperature(self):
        del self._celsius

temp = TemperatureConverter(25)

print(temp.temperature)

temp.temperature = 30
print(temp.temperature)

del temp.temperature
print(temp.temperature)