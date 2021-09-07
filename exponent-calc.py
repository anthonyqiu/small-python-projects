
num1 = int(input("Enter a base: "))
num2 = int(input("Enter a power: "))


def raise_to_power(base, power):
    result = 1
    for index in range(power):
        result = result * base
    return result

print(raise_to_power(num1, num2))
