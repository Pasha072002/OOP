# Arithmetic Operators
number = 1 + 2 * 3 / 4.0
print(number)

remainder = 11 % 3
print(remainder)

squeared = 7 ** 2
cubed = 2 ** 3
print(squeared)
print(cubed)

# Using Operators with Strings
helloworld = "hello" + " " + "world"
print(helloworld)

lotsofhellos = "hello" * 10
print(lotsofhellos)

# Using Operators with Lists

even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

print([1,2,3] * 3)

print("--------------------------------")
print("Exercise")
print("Метою цієї вправи є створення двох списків із назвою x_list та y_list, які містять 10 екземплярів змінних x та y відповідно. ")
print("Вам також потрібно створити список під назвою big_list, який містить змінні x та y, по 10 разів кожна, шляхом об’єднання двох створених вами списків.")
print("--------------------------------")

x = object()
y = object()

x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list містить %d об'єктів" % len(x_list))
print("y_list містить %d об'єктів" % len(y_list))
print("big_list містить %d об'єктів" % len(big_list))

if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Майже готово...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")