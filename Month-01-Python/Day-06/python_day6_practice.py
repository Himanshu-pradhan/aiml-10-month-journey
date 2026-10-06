1. Create a tuple of 5 numbers.

numbers = (1, 2, 3, 4, 5)
print (type(numbers))
print(numbers)

# 2. Print first and last element

numbers = (10, 20, 30, 40, 50)

print("first :", numbers[0])
print("last : ", numbers[-1])

#3. find length of tuple

numbers = (10, 20, 30, 40, 50)

print("length : ", len(numbers))

# 4. Check if a value is present in tuple

numbers = (10, 20, 30, 40, 50)

if  30 in numbers:
    print("it is there")
else:
    print("there is not ")

# 5. Print all tuple elements using for loop

numbers = (10, 20, 30, 40, 50)

for number in numbers:
    print(numbers)

# 6. Create a set with duplicate values 

numbers = {10, 20, 30, 40, 50, 50, 20, 30}

print(numbers)

# 7. Add a new number to set

numbers = {10, 20, 30, 40, 50}
numbers.add(60)
print(numbers)


# 8. Remove a number from a set

numbers = {10, 20, 30, 40, 50}

numbers.remove(10)

print(numbers)

# 9. Find union of two sets 

a = {1, 2, 3}
b = {4, 5, 6}

result = a.union(b)

print(result)

# 10. Find intersection of two sets

a = {1, 2, 3}
b = {3, 4, 5}

result = a.intersection(b)

print (result)













