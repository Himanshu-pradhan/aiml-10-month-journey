# 1. Store name, age and city in a dictionary

detials ={
    "name" : "Himanshu",
    "std" : "BA",
    "city" : "Ramnagar",
    "age" : 25
}

print(detials)

# 2. print name from dictionary

person = {
    "name" : "Himanshu",
    "age" : 22,
    "city" : "Ramnagar"
}

print(person["name"])

# 3. Add a new college key

person = {
    "name" : "Himanshu",
    "age" : 22,
    "city" : "Ramnagar"

}
person["college"] = "Parul"

print(person)


# 4. Change age

person = {
    "name" : "Himanshu",
    "age" : 22,
    "city" : "Ramnagar"
}


person["age"] = 26

print(person)

# 5. Delete city

person = {
    "name": "Himanshu",
    "age": 21,
    "city": "Vadodara"
}

del person["city"]

print(person)


# 6. Print all keys

person = {
    "name": "Himanshu",
    "age": 21,
    "city": "Vadodara"
}

for key in person:
    print(key)


# 7. Print all values

person = {
    "name": "Himanshu",
    "age": 21,
    "city": "Vadodara"
}

for key in person:
    print(person[key])


# 8. Print key and value together

person = {
    "name": "Himanshu",
    "age": 21,
    "city": "Vadodara"
}

for key in person:
    print(key, person[key])


# 9. Store 5 students and their marks

students = {
    "Rahul": 85,
    "Aman": 92,
    "Riya": 78,
    "Neha": 88,
    "Karan": 95
}

print(students)


# 10. Find student with highest marks

students = {
    "Rahul": 85,
    "Aman": 92,
    "Riya": 78,
    "Neha": 88,
    "Karan": 95
}

highest_marks = 0
top_student = ""

for name in students:
    if students[name] > highest_marks:
        highest_marks = students[name]
        top_student = name

print("Top student:", top_student)
print("Marks:", highest_marks)






















