# The LEGB rule in Python defines the order in which Python looks for variables.
# L - Local: Variables defined inside a function.
# E - Enclosed: Variables in the scope of an enclosing function (for nested functions).
# G - Global: Variables defined at the top level of a module.
# B - Built-in: Python's pre-defined names (e.g., print, len).

# -----------------
# L - LOCAL SCOPE
# -----------------
def local_example():
    x = 10  # This 'x' is local to local_example()
    print("Local scope:", x)

local_example()

# -----------------
# E - ENCLOSED SCOPE
# -----------------
def enclosed_example():
    y = 20  # This 'y' is in the enclosed scope for inner_func()
    
    def inner_func():
        print("Enclosed scope:", y)
    
    inner_func()

enclosed_example()

# -----------------
# G - GLOBAL SCOPE
# -----------------
z = 30  # This 'z' is in the global scope

def global_example():
    print("Global scope:", z)

global_example()

# A function can also modify a global variable using the 'global' keyword.
def modify_global():
    global z  # Declares that we are using the global 'z'
    z = 40
    print("Modified global scope:", z)

modify_global()
print("Global 'z' after modification:", z)

# -----------------
# B - BUILT-IN SCOPE
# -----------------
# The 'print' function is a perfect example of a built-in.
# You don't need to import it or define it yourself; it's always available.
print("Hello, this is a built-in function!")

# The 'len' function is another built-in.
my_list = [1, 2, 3, 4, 5]
length_of_list = len(my_list)
print("The length of the list is:", length_of_list)

# You can even check for built-ins in the current scope using the 'dir' function.
# This is a bit more advanced but demonstrates the concept.
import builtins
print(dir(builtins)) # This will output a list of all built-in names