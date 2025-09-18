#super() = Function used in a child class to call methods from a parent class (superclass)
#Allows you to extend the functionality of the inherited methods

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled


    def describe(self):
        print(f"it's color is {self.color} and {"filled" if self.is_filled else "not filled "}")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        print(f"the area of that circle is {3.14*self.radius*self.radius}")
        super().describe() #self() make circle.describe() print both describe methods in shape and circle class
                           #as well as square class unlike the triangle class

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width
    
    def describe(self):
        print(f"the area of that square is {self.width*self.width}")
        super().describe()

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        print(f"the area of that square is {0.5*self.width*self.height}")
        #❌❌❌ no super function which lead to describe what in the triangle 
        #method(fuction) only not also what in the shape method

circle=Circle(color="red", is_filled=True, radius=10)
square=Square(color="blue", is_filled=False, width=20)
triangle=Triangle(color="yellow", is_filled=True, width=15, height=30)

print(circle.color)
print(circle.is_filled)
print(circle.radius)

circle.describe() 

"""insted of :

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        self.color = color
        self.is_filled = is_filled
        self.radius = radius

class Square(Shape):
    def __init__(self, color, is_filled, width):
        self.color = color
        self.is_filled = is_filled
        self.width = width

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        self.color = color
        self.is_filled = is_filled
        self.width = width
        self.height = height """
