from car import Car

# object = "A bundle" of related attributes (variables) and methods (functions)
# Ex. phone, cup, book
# You need a "class" to create many objects

# class = (blueprint) used to design the structure and layout of an object

car1 = Car("Mustang", 2024, "red", False)
car2 = Car("Corvette", 2025, "blue", True)
car3 = Car("Charger", 2026, "yellow", True)

print(car2.model)
print(car2.year)
print(car2.color)
print(car2.for_sale)
car3.describe()

print("-----")

# Call methods on car1
car1.describe()    # 2025 red Tesla Model S
car1.drive()       # You drive the red Tesla Model S
car1.stop()        # You stop the red Tesla Model S

print("-----")

# Call methods on car2
car2.describe()    # 2023 black BMW X5
car2.drive()       # You drive the black BMW X5
car2.stop()        # You stop the black BMW X5


