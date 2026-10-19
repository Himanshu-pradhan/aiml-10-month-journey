# 1. Create a 2D list containing 3 rows and 3 columns, then print it.

numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(numbers)

# 2. Print the first element of the first row.

numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(numbers[0][0])

# 3. Print the last element of the second row.

numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(numbers[1][-1])

# 4. Print all elements of a 2D list using nested loops.

numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in numbers:
    for num in row:
        print(num)

# 5. Find the sum of all numbers in a 2D list.

numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

total = 0

for row in numbers:
    for num in row:
        total = total + num

print("Sum:", total)

# 6. Count how many even numbers are present in a 2D list.

numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

count = 0

for row in numbers:
    for num in row:
        if num % 2 == 0:
            count = count + 1

print("Even numbers:", count)

# 7. Find the largest number in a 2D list.

numbers = [
    [10, 25, 3],
    [45, 12, 6],
    [7, 80, 9]
]

largest = numbers[0][0]

for row in numbers:
    for num in row:
        if num > largest:
            largest = num

print("Largest:", largest)

# 8. Print each row of a 2D list on a separate line.

numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in numbers:
    print(row)

# 9. Calculate the sum of each row in a 2D list.

numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in numbers:
    total = 0

    for num in row:
        total = total + num

    print("Row sum:", total)

# 10. Write a function that returns the total number of elements in a 2D list.

def count_elements(numbers):
    count = 0

    for row in numbers:
        for num in row:
            count = count + 1

    return count


numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(count_elements(numbers))



















