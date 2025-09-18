#Inheritance = Allows a class to inherit attributes and methods from another class
#Helps with code reusability and extensibility
#class Child(Parent)


class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is asleep")


class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking")


class Cat(Animal):
    def meow(self):
        print(f"{self.name} is meowing")


class Mouse(Animal):
    def squeak(self):
        print(f"{self.name} is squeaking")


# Creating instances of the subclasses
dog = Dog("Buddy")
cat = Cat("Whiskers")
mouse = Mouse("Jerry")

# Calling methods from the parent class (Animal)
print(f"Is {dog.name} alive? {dog.is_alive}")
dog.eat()
dog.sleep()

print(f"\nIs {cat.name} alive? {cat.is_alive}")
cat.eat()
cat.sleep()

print(f"\nIs {mouse.name} alive? {mouse.is_alive}")
mouse.eat()
mouse.sleep()


# Calling methods from the specific subclasses
print("\n--- Calling subclass-specific methods ---")
dog.bark()
cat.meow()
mouse.squeak()