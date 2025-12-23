# Printing numbers from 1 to 10 using for loop
for i in range(1, 11):
    print(i)

# Printing even numbers from 1 to 10
for i in range(1, 11):
    if i % 2 == 0:
        print(i)

# Printing odd numbers from 1 to 10
for i in range(1, 11):
    if i % 2 != 0:
        print(i)

# Sum of numbers from 1 to 10 using for loop
total = 0
for i in range(1, 11):
    total += i
print("Sum:", total)

# Printing multiples of 3 and * for other numbers from 1 to 24
for i in range(1, 25):
    if i % 3 == 0:
        print(i)
    else:
        print("*")
