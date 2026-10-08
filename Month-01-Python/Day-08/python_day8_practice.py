# 1. get() se name print karo

student = {
    "name" : "Himanshu",
    "age" : 22,
    "marks" : 42,
    "city" : "Ramnagar"

}

print(student.get("name"))


# 2. print all keys

student = {
    "name" : "Himanshu",
    "age" : 22,
    "marks" : 42,
    "city" : "Ramnagar"
}

for key in student:
    print(key)


# 3. Print all values

student = {
    "name" : "Himanshu",
    "age" : 22,
    "marks" : 42,
    "city" : "Ramnagar"
}

for key in student:
    print(student[key])


# 4. print both key and values

student = {
    "name" : "Himanshu",
    "age" : 22,
    "marks" : 42,
    "city" : "Ramnagar"
}

for key, value in student.items():
    print(key, value)

# 5. Check the age key present or not.

student = {
    "name" : "Himanshu",
    "age" : 22,
    "marks" : 42,
    "city" : "Ramnagar"
}

if "age" in student:
    print("present")
else:
    print("not present")


# 6. Check the student fail/pass.

student = {
    "name" : "Himanshu",
    "age" : 22,
    "marks" : 42,
    "city" : "Ramnagar"
}

if student["marks"] >= 40:
    print("pass")
else:
    print("fail")

# 7. Find the highest mark student.

students = {
    "Rahul": 85,
    "Aman": 92,
    "Riya": 78,
    "Neha": 88
}

highest_marks = 0
top_Student = "" 

for name in student:
    if student[name] > highest_marks:
        highest_marks = student[name]
        top_Student = name

print("Top student :", top_Student)
print("Marks : ", highest_marks)


# 8. Add 5 marks to every student's marks.

students = {
    "Rahul": 80,
    "Aman": 70,
    "Riya": 90
}

for name in students:
    students[name] = students[name] + 5

print(students)


# 9. Check whether "college" exists. If not, add it.

student = {
    "name": "Himanshu",
    "age": 21
}

if "college" not in student:
    student["college"] = "ABC College"

print(student)


# 10. Print the names of students who scored 50 or more.

students = {
    "Rahul": 45,
    "Aman": 78,
    "Riya": 32,
    "Neha": 90,
    "Karan": 55
}

for name in students:
    if students[name] >= 50:
        print(name)










