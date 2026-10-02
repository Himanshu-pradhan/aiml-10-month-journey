# DAY 2 - IF / ELIF / ELSE PRACTICE

# Q1
num = float(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# Q2
age = int(input("Enter your age: "))

if age >= 18:
    print("Adult")
else:
    print("Minor")


# Q3
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# Q4
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)


# Q5
marks = float(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")


# Q6
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid Credentials")


# Q7
num = int(input("Enter a number: "))

if num % 5 == 0 and num % 11 == 0:
    print("Divisible by both 5 and 11")
else:
    print("Not divisible by both 5 and 11")


# Q8
temperature = float(input("Enter temperature: "))

if temperature >= 35:
    print("Very Hot")
elif temperature >= 25:
    print("Hot")
elif temperature >= 15:
    print("Normal")
else:
    print("Cold")


# Q9
year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")


# Q10
units = float(input("Enter electricity units: "))

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = units * 7
elif units <= 300:
    bill = units * 10
else:
    bill = units * 15

print("Electricity Bill:", bill)
