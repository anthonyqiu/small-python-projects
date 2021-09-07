num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "Add":
    print(num1 + num2)
elif op == "Subtract":
    print(num1 - num2)
elif op == "Multiply":
    print(num1 * num2)
elif op == "Divide":
    print(num1 / num2)
else:
    print("Operation not supported with this calculator")
