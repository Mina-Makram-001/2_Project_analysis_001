#heart assy. by nested loops

import time

print("let rows and colomuns = 6 ")
row=int(input("inter the no. of rows : ")) 
colomun=int(input("inter the no. of colomun : "))
s=input("inter any symbol : ")

for x in range (1, row):
    for y in range (1, colomun):
        if (x==2 and y==1) or\
        (x==3 and y==1) or\
        (x==1 and y==2) or\
        (x==4 and y==2) or\
        (x==2 and y==3) or\
        (x==5 and y==3) or\
        (x==1 and y==4) or\
        (x==4 and y==4) or\
        (x==2 and y==5) or\
        (x==3 and y==5):
            print(s, end=" ")
            time.sleep(2)
        else:
            print(" ", end=" ")  
    print()
