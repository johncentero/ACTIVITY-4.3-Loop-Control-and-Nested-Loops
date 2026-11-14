#TERO, JOHN CEN O.
#BAET 2101

total = 0
numbers = []

for n in range(1, 51):
    if n % 3 == 0:
        continue
    numbers.append(n)
    total += n

print(*numbers)
print("Sum:", total)