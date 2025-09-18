#Polymorphism = Greek word that means to "have many forms or faces"
#Poly = Many
#Morphe = Form

#TWO WAYS TO ACHIEVE POLYMORPHISM
#1. Inheritance = An object could be treated of the same type as a parent class
#2. "Duck typing" = Object must have necessary attributes/methods

from abc import ABC, abstractmethod

# ده الكلاس الأساسي (القالب)
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


# كلاس الدائرة يرث من Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


# كلاس المربع يرث من Shape
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


# كلاس المثلث يرث من Shape
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


# بنعمل ليست من الأشكال
shapes = [Circle(5), Square(4), Triangle(6, 8)]

# بنطبع المساحات
for shape in shapes:
    print(f"The area of the shape is: {shape.area()} cm²")

"""
✅ Difference in Simple Terms
Inheritance Polymorphism:
Classes are forced to follow a shared structure (interface/abstract base class).
Safer: you're guaranteed all subclasses have the same method.
More strict and organized.
Duuk Typing Polymorphism:
No need for a common parent class.
More flexible but less safe: if an object doesn't have the expected method, it crashes.
Used often in Python because Python values flexibility."""


