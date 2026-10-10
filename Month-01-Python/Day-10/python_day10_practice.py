# 1. Create a list of square of numbers from 1 to 10

numbers = [num * num for num in range(1, 11)]
print(numbers)

# 2. Create a list of even numbers from 1 to 20.

even_numbers = [num for num in range(1, 21) if num % 2 == 0]

print(even_numbers)

# 3. Create a list of odd numbers from 1 to 10.

odd_numbers = [num for num in range(1, 11) if num % 2 != 0]
print(odd_numbers)

# 4. Create a list of squares of even numbers from 1 to 10.

squares = [num * num for num in range(1, 11) if num % 2 == 0]
print(squares)

# 5. Convert all words in a list to uppercase.

words = ["apple", "banana", "mango", "litchi"]

new_words =[word.upper() for word in words]

print(new_words)

# 6. Create a list of numbers greater than 10.

numbers = [5, 12, 8, 20, 15, 3]

result = [num for num in numbers if num > 10]

print(result)

# 7. Create a list of length of the given words.

words = ["apple", "banana", "city", "Ramnagar"]

lengths = [len(word) for word in words]

print(lengths)

# 8. Create a list of numbers divisible by both 3 and 5 from 1 to 100.

numbers = [ num for num in range(1, 101) if num % 3 == 0 and num % 5 == 0]

print(numbers)

# 9. Create a list of positive numbers.

numbers = [-5, 10, -2, 8, 0, 15, -7]

positive = [num for num in numbers if num > 0]

print(positive)

# 10. Write a function that returns the square of every number in a list.

def square_numbers(numbers):
    result = []

    for num in numbers:
        result.append(num * num)

    return result

numbers = [2, 3, 4, 5]

print(square_numbers(numbers))





















