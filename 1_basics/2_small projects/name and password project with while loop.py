#name and password project with while loops.

correctname="mina"
correctpass="123mina"

name=input("inter your name : ")
password=input("inter your password : ")

while name=="" or password=="":
    print("please inter your name and password")
    
    if name=="":
        name=input("inter your name : ")
    elif password=="":
        password=input("inter your password : ")

while not name==correctname or not password==correctpass:
    print("either your name or your password is wrong")
    name=input("inter your name : ")
    password=input("inter your password : ")
    

print(f"welcome {name}")