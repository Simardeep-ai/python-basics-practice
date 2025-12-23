student = {
    "name": "Simardeep",
    "course": "AI/ML",
    "semester": 1
}
print(student)

# Accessing values using keys
print(student["name"])
print(student["course"])

# Adding a new key-value pair
student["Age"] = 17
print(student)

# Updating an existing value
student["semester"] = 2
print(student)

# Looping through dictionary keys and values
for key, value in student.items():
    print(key, ":", value)

# Printing only keys and values
print("Keys:", student.keys())
print("Values:", student.values())
