#1. Print 1 to 10

for i in range(1, 11):
    print(i)


#2. Print 10 to 1

for i in range(10, 0, -1):
    print(i)


#3. Print even numbers from 1 to 20

for i in range(1, 21):
    if i % 2 == 0:
        print(i)


#4. Sum of numbers from 1 to 10

total = 0

for i in range(1, 11):
    total = total + i

print("Sum =", total)


#5. Sum from 1 to n

n = int(input("Enter a number: "))
total = 0

for i in range(1, n + 1):
    total = total + i

print("Sum =", total)


#6. Multiplication table

n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)


#7. Count numbers divisible by 3

count = 0

for i in range(1, 101):
    if i % 3 == 0:
        count = count + 1

print("Count =", count)


#8. Factorial

n = int(input("Enter a number: "))
factorial = 1

for i in range(1, n + 1):
    factorial = factorial * i

print("Factorial =", factorial)


#9. Stop the loop at 40

for i in range(1, 51):
    if i == 41:
        break
    print(i)


#10. Skip multiples of 5

for i in range(1, 21):
    if i % 5 == 0:
        continue
    print(i)
