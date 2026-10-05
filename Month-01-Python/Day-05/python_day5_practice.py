# 1. Create a list of 5 numbers and print it

numbers = [10, 15, 20, 40, 23]
print(numbers)


# 2.Print first and last element

numbers = [10, 20, 30 ,40 , 50]

print("first :",numbers[0])
print("last : ", numbers[-1])

# 3.Add a new number using append()

numbers = [10, 20, 30 , 40, 50]
numbers.append(60)
print(numbers)

# 4.Change an element

text = ["apple", "banana", "cat", "dog"]

text[1] = "fish"

print(text)


# 5. Remove an element

numbers = [10, 20, 30, 40]
numbers.remove(20)

print(numbers)


# 6. Find length of list

numbers = [10, 20, 30, 40, 50]

print("Length:", len(numbers))


# 7. Print all elements using for loop

numbers = [10, 20, 30, 40, 50]

for number in numbers:
    print(number)


# 8. Find sum of all numbers

numbers = [10, 20, 30, 40]
total = 0

for number in numbers:
    total = total + number

print("Sum:", total)


# 9. Find the largest number

numbers = [10, 45, 23, 67, 12]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print("Largest:", largest)


# 10. Count even numbers

numbers = [10, 15, 20, 25, 30, 35]
count = 0

for number in numbers:
    if number % 2 == 0:
        count = count + 1





























