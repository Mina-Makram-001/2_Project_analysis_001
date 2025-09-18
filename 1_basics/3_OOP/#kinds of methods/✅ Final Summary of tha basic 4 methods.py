#✅ Final Summary of tha basic 3 methods
#Instance method → object-level behavior.
#Class method → class-level behavior.
#Static method → helper, doesn’t touch class or object.
#Magic method → special hooks Python calls automatically (customize operators & built-ins).

"""🔹 1. Instance Methods
First parameter = self (the object itself).
Can access instance attributes (unique to each object).
Can also access class attributes, but usually used for per-object data."""

class Student:
    def __init__(self, name):
        self.name = name   # instance attribute
    
    def say_hello(self):   # instance method
        print(f"Hello, I am {self.name}")

s1 = Student("Mina")
s1.say_hello()   # ✅ works → bound to object


"""🔹 2. Class Methods
First parameter = cls (the class itself).
Can access/modify class attributes (shared by all objects).
Often used as factory methods (alternative constructors)."""

class Student:
    school = "Cairo University"   # class attribute
    
    def __init__(self, name):
        self.name = name
    
    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school   # affects ALL students

Student.change_school("Oxford")
print(Student.school)   # Oxford


"""🔹 3. Static Methods
No self, no cls.
Behave like normal functions, but are put inside a class for organization.
Don't touch class or instance data — they just do something useful."""

class MathTools:
    @staticmethod
    def add(a, b):   # static method
        return a + b
    
print(MathTools.add(3, 4))   # 7


"""🔹 4. Magic (Dunder) Methods
Their names start and end with double underscores → __like_this__.
They are special methods that Python automatically calls in certain situations.
They make your objects behave like built-in Python types.
✅ Common Examples
__init__ → Constructor (called when you create an object).
__str__ → What shows when you print(obj).
__len__ → Makes your object usable with len(obj).
__add__ → Defines how + works for your object."""

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):         # string representation
        return f"({self.x}, {self.y})"
    
    def __add__(self, other):  # define + operator
        return Vector(self.x + other.x, self.y + other.y)

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1)       # (1, 2) → __str__
print(v1 + v2)  # (4, 6) → __add__
