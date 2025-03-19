first_value = float(input("Enter first value: "))
second_value = float(input("Enter second value: "))
operation = input("Enter operation: ")

if operation == "+":
    print(first_value + second_value)
elif operation == "-":
    print(first_value - second_value)
elif operation == "*":
    print(first_value * second_value)
elif operation == "/":
    print(first_value / second_value)
else:
    print("Invalid operation")