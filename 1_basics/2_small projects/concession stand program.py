#concession stand program

menu = {
    "pizza": 3.00,
    "nachos": 4.50,
    "popcorn": 6.00,
    "fries": 2.50,
    "chips": 1.00,
    "pretzel": 3.50,
    "soda": 3.00,
    "lemonade": 4.25
}

cart=[]
total=0

print("--------menu--------")
for key, value in menu.items():
    print(f"{key:10}: {value:2f}")
print("--------------------")
print()

while True:
    food=input("inter what you want from the menu : ").lower()
    if food=="q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
print()

print("-----your order-----")
for food in cart:
    print(food)
    total+=menu.get(food)
print()

print(f"for what you buy you should pay {total:2f}$")