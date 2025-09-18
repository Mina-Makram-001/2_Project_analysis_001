#List comprehension = A concise way to create lists in Python
#Compact and easier to read than traditional loops
#[expression for value in iterable if condition]

doubles = []
for x in range(1, 11):
    doubles.append(x * 2)

print(doubles)



doubles = [x * 2 for x in range(1, 11)]
print(doubles)
