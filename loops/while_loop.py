# Printing numbers from 0 to 10 using while loop
i = 0
while i <= 10:
    print(i)
    i += 1

# Printing even numbers from 0 to 20 using while loop
i = 0
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1

# Printing odd numbers from 0 to 20 using while loop
i = 0
while i <= 20:
    if i % 2 != 0:
        print(i)
    i += 1

# Finding sum of numbers from 0 to 20 using while loop
i = 0
total = 0
while i <= 20:
    total += i
    i += 1
print("Sum:", total)

# Printing multiples of 3 and * for other numbers from 0 to 24
i = 0
while i < 25:
    if i % 3 == 0:
        print(i)
    else:
        print("*")
    i += 1
