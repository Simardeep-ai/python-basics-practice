def str():
    print("Hello")
str()

def add(a, b):
    print("Sum:", a + b)

add(5, 3)

# Function that returns a value
def multiply(a, b):
    return a * b

result = multiply(4, 6)
print("Result:", result)

# Function to check even or odd
def check_even_odd(num):
    if num % 2 == 0:
        print(num, "is even")
    else:
        print(num, "is odd")

check_even_odd(7)

# Function using list
def print_list(items):
    for i in items:
        print(i)

print_list([1, 2, 3, 4])
