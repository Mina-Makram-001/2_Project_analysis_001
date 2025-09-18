def my_name(name,age):
    print("my name is "+name+" my age is "+str(age))
my_name("mina",20)

def my_name():
    name=input("your name is ? ")
    age=str(input("your age is ? "))
    print("my name is "+name+" my age is "+str(age))
my_name()

def my_name():
    name = input("Your name is? ")
    age = input("Your age is? ")
    print(f"My name is {name}, and my age is {age}.")
my_name()

def cube(num):
    return num*num*num

X=cube(10)
print(X)

print("__________________________________________________________________")

from math import*

print("if aX^2 + bX + c=0")
no1=float(input("no.1 is : "))
no2=float(input("no.2 is : "))
no3=float(input("no.3 is : "))

def x_equal_what(a,b,c):
    root1 = (-b + sqrt(b**2- 4 * a * c))/(2*a)
    root2 = (-b - sqrt(b**2- 4 * a * c))/(2*a)
    return root1 , root2

M=x_equal_what(no1,no2,no3)
print(M)
