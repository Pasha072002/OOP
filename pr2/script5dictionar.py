# Dictionaries

#1
phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)

#2
phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
print(phonebook)

#3 Перегляд словників
phonebook = {"John" : 938477566, "Jack" : 938377264, "Jill" : 947662781}
for name, number in phonebook.items():
    print("Phone number of %s si %d" % (name, number))

#3 Видалення словників
phonebook = {
   "John" : 938477566,
   "Jack" : 938377264,
   "Jill" : 947662781
}
del phonebook["John"]
print(phonebook)

print("--------------------------------")
print("Exercise")
print("Додайте 'Jake' до телефонної книги з номером 938273443 і видаліть Jill з телефонної книги")
print("--------------------------------")

phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}

phonebook["Jake"] = 938273443
del phonebook["Jill"]

# testing code
if "Jake" in phonebook:
    print("Jack занесений у телефонну книгу.")
if "Jill" not in phonebook:
    print("Jill не занесений у телефонний книгу")