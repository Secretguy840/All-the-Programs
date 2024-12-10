# Simple Calculator Program in Python

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
        return "Error! Division by zero."

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # Get user input for the operation
    choice = input("Enter choice (1/2/3/4): ")

    # Check if the input is valid
    if choice in ['1', '2', '3', '4']:
        # Get numbers from the user
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # Perform the operation based on user choice
        if choice == '1':
            print(f"The result of addition is: {add(num1, num2)}")
        elif choice == '2':
            print(f"The result of subtraction is: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"The result of multiplication is: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"The result of division is: {divide(num1, num2)}")
    else:
        print("Invalid input! Please choose a valid operation (1/2/3/4).")

# Run the calculator
calculator()
