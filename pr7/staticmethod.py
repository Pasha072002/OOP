class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

result_add = Calculator.add(5, 3)  
print("Результат додавання:", result_add)  

result_subtract = Calculator.subtract(10, 4)  
print("Результат віднімання:", result_subtract)