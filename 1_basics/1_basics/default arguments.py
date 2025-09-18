#default arguments= a default value for certain parameters
#                    is used when that argument is omitted
#                    function calls. Make functions more flexible.
#                    reduces # of arguments.
#                    1. positional
#                    2. default
#                    3. keyword
#                    4. arbitrary


#positional arguments

def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")

hello("Hello", "Mr.", "Spongebob", "Squarepants")

#default arguments= a default value for certain parameters
#                    is used when that argument is omitted
#                    function calls.

def net_price(list_price, discount=0.05, tax=0.05):
    return list_price * (1 - discount) * (1 + tax)

print(net_price(500))         # uses default discount=0.05, tax=0.05
print(net_price(500, 0.1))    # overrides discount=0.1, keeps tax=0.05
print(net_price(500, 0.1, 0)) # overrides both discount=0.1, tax=0

import time

def count(end, start=0):
    for x in range(start, end + 1):
        print(x)
        time.sleep(1)

count(30, 26)
print("DONE!")


#keyword arguments= an argument preceded by an identifier
#                    helps with readability
#                    order of arguments doesn't matter


def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")

hello("Hello", title="Mr.", first="Spongebob", last="Squarepants") #default arguments should be before keyword arguments

for x in range(1, 11):
    print(x, end=" ")

print(1, 2, 3, 4, 5, sep="-")


#arbitrary arguments

# *args   = allows you to pass multiple non-key arguments--> used as a tuple 
# **kwargs = allows you to pass multiple keyword arguments--> used as a dictionary

#example1_*args--> used as tuples
def add(*args):
    print(type(args))

print(add(1, 2, 3))

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1, 2, 3))

#example2_**kwargs--> used as dictionaries
def print_address(**kwargs):
    print(type(kwargs))

print_address(
    street="123 Fake St.",
    apt="100",
    city="Detroit",
    state="MI",
    zip="54321"
)

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(
    street="123 Fake St.",
    apt="100",
    city="Detroit",
    state="MI",
    zip="54321"
)

#example3_*args and **kwargs
def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('city')}, {kwargs.get('state')}, {kwargs.get('zip')}")

shipping_label("Dr.", "Spongebob", "Squarepants", "III",
               street="123 Fake St.",
               apt="100",
               city="Detroit",
               state="MI",
               zip="54321")

print("\n--------------------------\n")

shipping_label("Dr.", "Spongebob", "Squarepants",
               street="123 Fake St.",
               pobox="PO Box #1001",
               city="Detroit",
               state="MI",
               zip="54321")