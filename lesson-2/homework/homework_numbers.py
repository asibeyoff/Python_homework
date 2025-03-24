# 1
x = float(input("Enter number: "))
print(f"2 decimal places: {x:.2f}")

# 2
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

largest = max(num1, num2, num3)
smallest = min(num1, num2, num3)

print(f"Largest: {largest}, Smallest: {smallest}")

# 3
km = float(input("Enter distance in kilometers: "))
meters = km * 1000
centimeters = km * 100000

print(f"{km} km is {meters} meters and {centimeters} centimeters.")

# 4
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

q = a // b
remainder = a % b

print(f"Quotient: {q}, Remainder: {remainder}")

# 5
celsius = float(input("Enter temperature in Celsius: "))
f = (celsius * 9/5) + 32

print(f"{celsius}°C is {f}°F")

# 6
num = int(input("Enter a number: "))
last_digit = abs(num) % 10

print(f"The last digit of {num} is {last_digit}")

# 7
number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")

