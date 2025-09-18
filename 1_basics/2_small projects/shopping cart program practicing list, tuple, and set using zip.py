# shopping cart program practicing list, tuple, and set using zip

foods = []
prices = []
total = 0

while True:
    food = input("Enter the food you want (or 'q' to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"The price of {food} is: "))
        foods.append(food)
        prices.append(price)

print("\n___ Your Cart ___")
for food, price in zip(foods, prices):
    print(f"You bought {food}, you paid {price:.2f} $")

total = sum(prices)
print(f"\nYour total is: {total:.2f} $")
