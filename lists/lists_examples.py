# Creating a list and accessing elements
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lst[0])    # first element
print(lst[4])    # element at index 4
print(lst[-1])   # last element

# Looping through a list
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in lst:
    print(i)

# Adding an element to the list
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lst.append(10)
print(lst)

# Removing an element from the list
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lst.remove(9)
print(lst)

# Finding length of the list
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Length:", len(lst))
