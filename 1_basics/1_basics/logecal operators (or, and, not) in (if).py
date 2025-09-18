#logecal operators (or, and, not) in (if)
#                   or= at leat one must be T
#                   and= all must be T
#                   not= inverts the condition

temp=float(input("inter the temp. :"))
is_sunny= True

if temp > 20 and is_sunny:
    print("it is hot")
    print("it is sunny")
elif temp < 15 and is_sunny:
    print("it is cold")
    print("it is sunny")
else:
    print("it is good")
    print("it is sunny")