def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

def exponent(x, y):
    return x**y
    
print("SIMPLE CALCULATOR")
print("-----------------")
while True:
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponent")
    print("6. Exit")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == '6':
        print("Exiting the calculator.")
        break

    if choice not in ('1', '2', '3', '4','5'):
        print("Invalid Input. Please enter a valid number (1/2/3/4/5).")
        continue

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))
    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))
    elif choice == '4':
        result = divide(num1, num2)
        print(num1, "/", num2, "=", result)
    elif choice == '5':
        print(num1, "power", num2, "=", exponent(num1, num2))
