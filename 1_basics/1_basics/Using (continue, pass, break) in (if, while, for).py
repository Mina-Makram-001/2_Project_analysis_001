#Using (continue, pass, break) in (if, while, for)
#notice that continue and break used only in loops (while, for)

#Using continue — Skip to the next iteration

for i in range(5):
    if i == 2:
        continue  # skip when i == 2
    print(i)

#Using pass — Do nothing (placeholder) pass just ignores that block but keeps the structure valid

x = 10
if x > 5:
    pass  # do nothing for now
print("Done")

#Using break — Exit the loop entirely

for i in range(5):
    if i == 3:
        break  # stop the loop completely
    print(i)
