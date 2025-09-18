#password only in no. notice that int make the output = a value of numbers not a string
try:
    password=int(input("inter your password ; ")) 
    var=7777
    if password == var:
        print ("the password is true")
    else:
        print("either your password or your email is wrong")
except ValueError:
    print("password should be in numbers")

#____________________________________________________________________#

#password in numbers & letters bec. we make line16 in "" unlike line4(is totally no. and thats why we had put int() at line3) 
password=input("inter your password ; ") 
var="123mina"
if password == var:
    print ("the password is true")
else:
    print("either your password or your email is wrong")
