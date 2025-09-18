#Decorator = A function that extends the behavior of another function
#            w/o modifying the base function
#            Pass the base function as an argument to the decorator

def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("You add sprinkles 🍨")
        func(*args, **kwargs)
    return wrapper #So wrapper = the decorated version of your function.
                   #It “wraps” extra code around your original function.

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("You add fudge 🍫")
        func(*args, **kwargs)
    return wrapper

@add_sprinkles #this is our decorators
@add_fudge 
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream 🍦")

get_ice_cream("vanilla")


#  ---- gpt explaination ----

"""1) What a decorator really is

A decorator is just a function that:

takes a function as input,

returns a new function that wraps extra behavior around the original.

Mathematically:
@A on function f means f = A(f).
With stacking:

@A
@B
def f(...): ...
# becomes:
f = A(B(f))


So when you call f(), it runs A's wrapper → which calls B's wrapper → which calls the original."""


"""*args and **kwargs

These let your wrapper accept any function signature:

*args = positional args tuple

**kwargs = keyword args dict

That way, your decorator works for any function, not just a specific one."""