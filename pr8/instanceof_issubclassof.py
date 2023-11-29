class A:
    pass

class B(A):
    pass

obj_b = B()

print(isinstance(obj_b, B))  # Виведе: True, оскільки obj_b є екземпляром класу B
print(isinstance(obj_b, A),"\n")  # Виведе: True, оскільки obj_b є екземпляром підкласу A (класу B)

print(issubclass(B, A))  # Виведе: True, оскільки B є підкласом A
print(issubclass(A, B))  # Виведе: False, оскільки A не є підкласом B