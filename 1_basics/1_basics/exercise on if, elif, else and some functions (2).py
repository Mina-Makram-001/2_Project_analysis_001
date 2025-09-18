#exercise on if, elif, else and some functions
name=input("inter your name : ")

if len(name)>12 :
    print("your max inputs should be 12 with no spaces or numbers")
elif not name.find(" ") ==-1:
    print("your max inputs should be 12 with no spaces or numbers")
elif not name.isalpha():
    print("your max inputs should be 12 with no spaces or numbers")
else:
    print(f"your name is {name}")