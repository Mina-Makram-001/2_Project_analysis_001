#Membership operators = used to test whether a value or variable is found in a sequence
#(string, list, tuple, set, or dictionary)

#1. in
#2. not in

grades = {"Sandy": "A",
          "Squidward": "B",
          "Spongebob": "C",
          "Patrick": "D"}

student = input("Enter the name of a student: ")

if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} was not found")
