# Strings 

print("String")
print("")

mystr = 'Pavlo'
print(mystr)
mystr = "Lara"
print(mystr)

one = 1
two = 2
t = one + two
print(t)

p = "Cell"
f = "Tetyana"
g = p + " " + f
print(g)

print("--------------------------------")
print("Exercise")
print("Вам потрібно буде написати рядок формату, який друкує дані за допомогою такого синтаксису: Hello John Doe. Your current balance is $53.44. ")
print("--------------------------------")
data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your currect balance is %s"
print( format_string % data)