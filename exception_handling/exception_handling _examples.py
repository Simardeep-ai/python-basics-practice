try:
    num = int(input("Enter a number: "))
    print(num)
except ValueError:
    print("Invalid input, please enter a number")

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(a / b)
except ZeroDivisionError:
    print("Cannot divide by zero")

try:
    x = int(input())
    print(10 / x)
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("Division by zero is not allowed")

try:
    num = int(input("Enter a number: "))
    print(num * num)
except ValueError:
    print("Invalid input")
else:
    print("Calculation successful")
finally:
    print("Program ended")
