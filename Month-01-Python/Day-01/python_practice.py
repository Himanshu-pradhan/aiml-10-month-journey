
# DAY 1 - PYTHON BASICS PRACTICE


# Q1. Greeting
name = input("Enter your name: ")
print("Hello", name, "Welcome to Python!")


# Q2. Two numbers - Sum, Difference, Product, Division
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)

if b != 0:
    print("Division:", a / b)
else:
    print("Division: Cannot divide by zero")


# Q3. Age after 5 years
age = int(input("Enter your age: "))
print("Your age after 5 years will be:", age + 5)


# Q4. Rectangle Area and Perimeter
length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width
perimeter = 2 * (length + width)

print("Area:", area)
print("Perimeter:", perimeter)


# Q5. Three Subjects - Total and Percentage
maths = float(input("Enter Maths marks: "))
python = float(input("Enter Python marks: "))
english = float(input("Enter English marks: "))

total = maths + python + english
percentage = total / 3

print("Total Marks:", total)
print("Percentage:", percentage)


# Q6. Celsius to Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print("Temperature in Fahrenheit:", fahrenheit)


# Q7. Remainder
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num2 != 0:
    print("Remainder:", num1 % num2)
else:
    print("Cannot find remainder because second number is zero")


# Q8. Square and Cube
number = float(input("Enter a number: "))

print("Square:", number ** 2)
print("Cube:", number ** 3)


# Q9. Simple Interest
principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time in years: "))

simple_interest = (principal * rate * time) / 100

print("Simple Interest:", simple_interest)


# Q10. Student Profile
student_name = input("Enter your name: ")
student_age = int(input("Enter your age: "))
college = input("Enter your college name: ")
branch = input("Enter your branch: ")

print("\n----- Student Profile -----")
print("Name:", student_name)
print("Age:", student_age)
print("College:", college)
print("Branch:", branch)
