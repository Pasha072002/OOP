class MyClass:
    def __init__(self, arg1, arg2, arg3):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.calc_attr = self.culculate_attribute()

    def culculate_attribute(self):
        return self.arg1 * self.arg2 + self.arg3
    

obj = MyClass(2, 67, 8)
print("arg1: ", obj.arg1)
print("arg2: ", obj.arg2)
print("arg3: ", obj.arg3)
print("calc_attr: ", obj.calc_attr)