#general formula calc. with while loops

from math import*

print("if aX^2 + bX + c = 0, to **get the REAL** value of x inter (a, b, c), notice that the equation should be b^2 - 4ac >= 0 ")
no1=float(input("no.1 is : "))
no2=float(input("no.2 is : "))
no3=float(input("no.3 is : "))

eq=no2**2- 4 * no1 * no3

while eq <= 0:
    print("if aX^2 + bX + c = 0, to **get the REAL** value of x inter (a, b, c), notice that the equation should be b^2 - 4ac >= 0 ")
    no1=float(input("no.1 is : "))
    no2=float(input("no.2 is : "))
    no3=float(input("no.3 is : "))
    

def x_equal_what(a,b,c):
    root1 = (-b + sqrt(b**2- 4 * a * c))/(2*a)
    root2 = (-b - sqrt(b**2- 4 * a * c))/(2*a)
    return root1 , root2

M=x_equal_what(no1,no2,no3)
print(M)