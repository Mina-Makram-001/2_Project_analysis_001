#nested loop = a loop within another loop (outer, inner)
#             outer loop:
#                  innerloop:
import time

row=int(input("inter the no. of rows : "))
colomun=int(input("inter the no. of colomuns : "))
sym=str(input("inter the used sympol : "))


for x in range(0, row):
    for y in range(0,colomun):
        print(sym, end="") # to make the no.s behind each other
    time.sleep(1)
    print() # to make the no.s above each other

#___________________________________________________

row=int(input("inter the no. of rows : "))
colomun=int(input("inter the no. of colomuns : "))


for x in range(0, row):
    for y in range(0,colomun):
        print(x, end="")
    time.sleep(1)
    print()