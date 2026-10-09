# 1. Write a function that print Hello World.

def greet():
    print("Hello, World")
greet()

# 2. Write a function that takes a name and prints a greeting.

def greet(name):
    print("Hello", name)

greet("Himanshu")

# 3. Write a function that takes two numbers and prints their sum.

def add(a , b):
    print(a + b)
add(10, 20)

# 4. Write a function that returns the square of a number.

def square(num):
    return num * num
answer = square (5)
print(answer)

# 5. Write a function that returns the larger of two numbers.

def largest(a, b):
    if a > b:
        return a
    else :
        return b

print(largest(10, 20))

# 6. Write a function that checks whether a number is even or odd.

def check(num):
    if num % 2 == 0:
        print("even")
    else :
        print("Odd")

check(7)

# 7. Write a function that returns the sum of numbers from 1 to n.

def total_sum(n):
    total = 0

    for num in range(1, n + 1):
        total = total + num

    return total

print(total_sum(5))

# 8. Write a function that prints the multiplication table of a number.

def table(num):
    for i in range(1, 11):
        print(num, 'x', i, "=", num * i)

table(5)

# 9. Write a function that counts the vowels in a string.

def count_vowels(text):
    count = 0

    for ch in text:
        if ch.lower() in "aeiou":
            count = count + 1

    return count

print(count_vowels("Himanshu"))

# 10. Write a function that checks whether a string is a palindrome.

def check_palindrome(text):
    if text == text[::-1]:
        return True
    else:
        return False

print(check_palindrome("madam"))























