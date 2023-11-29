# the "for" loop
primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)

for x in range(5):
    print(x)

for x in range(3, 6):
    print(x)

for x in range(3, 8, 2):
    print(x)

print("")
# "while" loop

count = 0
while count < 5:
    print(count)
    count += 1 

print("")
# "break" and "continue" statements

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

for x in range(10):
    if x % 2 == 0:
        continue
    print(x)

print("")
#Example loop
# Роздрукуй 0,1,2,3,4, а потім друкує "значення підрахунку досягнуто 5"
print("Exapmle")
count=0
while(count<5):
    print(count)
    count += 1
else:
    print("значення лічильника досягнуто %d" %(count))

for i in range(1, 10):
    if(i % 5== 0):
        break
    print(i)
else:
    print("це не друкується, тому що цикл for завершується через розрив, але не через несправність")