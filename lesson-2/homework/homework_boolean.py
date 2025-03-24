#1
username = input("Enter username: ")
password = input("Enter password: ")

if len(username) > 0 and len(password) > 0:
    print("Username and password are valid.")
else:
    print("Username and password cannot be empty.")
# 2
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 == num2:
    print("The numbers are equal.")

# 3
number = int(input("Enter a number: "))

if number > 0 and number % 2 == 0:
    print("The number is positive and even.")

# 4
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 != num2 and num1 != num3 and num2 != num3:
    print("All numbers are different.")

# 5
a = input("Enter first : ")
b = input("Enter second: ")

if len(a) == len(b):
    print("Both strings have the same length.")

# 6
num = int(input("Enter a number: "))

if num % 3 == 0 and num % 5 == 0:
    print("The number is divisible by both ")

# 7
num1 = int(input("Enter first : "))
num2 = int(input("Enter second : "))

if num1 + num2 > 50:
    print("The sum  greater than 50.")

# 8
num = int(input("Enter a number: "))

if 10 <= num <= 20:
    print("The number is between 10 20")

