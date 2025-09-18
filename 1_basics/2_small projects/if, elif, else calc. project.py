#if, elif, else calc. project

operation=input("choose an operator (+ - * /) : ")

num1=float(input("what is the 1st no. : "))
num2=float(input("what is the 2nd no. : "))

if operation == "+":
    result= num1+num2
    print(round(result, 3))
elif operation == "-":
    result= num1-num2
    print(round(result, 3))
elif operation == "*":
    result= num1*num2
    print(round(result, 3))
elif operation == "/":
    result= num1/num2
    print(round(result, 3))
else:
    print("choose a valid aperator please")
