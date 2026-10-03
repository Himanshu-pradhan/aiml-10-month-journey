#DAY 3 - LOOPS PRACTICE

#1. Print numbers from 1 to 10
print("Q1")

for i in range(1, 11):
    print(i)


#2. Print numbers from 10 to 1
print("\nQ2")

for i in range(10, 0, -1):
    print(i)


#3. Print even numbers from 1 to 20
print("\nQ3")

for i in range(2, 21, 2):
    print(i)


#4. Find the sum of numbers from 1 to 10
print("\nQ4")

total = 0

for i in range(1, 11):
    total = total + i

print("Sum:", total)


#5. Take n from user and find sum from 1 to n
print("\nQ5")

n = int(input("Enter n: "))
total = 0

for i in range(1, n + 1):
    total = total + i

print("Sum:", total)


#6. Multiplication table
print("\nQ6")

number = int(input("Enter a number: "))

for i in range(1, 11):
    print(number, "x", i, "=", number * i)


#7. Count numbers divisible by 3 from 1 to 100
print("\nQ7")

count = 0

for i in range(1, 101):
    if i % 3 == 0:
        count = count + 1

print("Count:", count)


#8. Find factorial of a number
print("\nQ8")

number = int(input("Enter a number: "))
factorial = 1

for i in range(1, number + 1):
    factorial = factorial * i

print("Factorial:", factorial)


#9. Use break stop after 40
print("\nQ9")

for i in range(1, 51):
    if i > 40:
        break

    print(i)


#10. Use continue skip multiples of 5
print("\nQ10")

for i in range(1, 21):
    if i % 5 == 0:
        continue

    print(i)
