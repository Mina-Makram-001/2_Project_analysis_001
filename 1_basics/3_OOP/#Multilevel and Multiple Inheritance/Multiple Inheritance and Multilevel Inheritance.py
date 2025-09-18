#Multiple Inheritance = inherit from more than one parent class
# C(A, B)

#Multilevel Inheritance = inherit from a parent which inherits from another parent
#C(B) <- B(A) <- A

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking.")


class Cat(Animal):
    def meow(self):
        print(f"{self.name} is meowing.")


class Mouse(Animal):
    def squeak(self):
        print(f"{self.name} is squeaking.")


class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing.")


class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting.")


# --- Multilevel Inheritance Example ---
class DomesticDog(Dog):
    def play(self):
        print(f"{self.name} is playing fetch.")


# --- Multiple Inheritance Example ---
class Bat(Predator, Prey):
    def fly(self):
        print(f"{self.name} is flying.")


# --- Example Usage ---

# Multilevel Inheritance
domestic_dog = DomesticDog("Max")
domestic_dog.eat()      # Inherited from Animal
domestic_dog.bark()     # Inherited from Dog
domestic_dog.play()     # Specific to DomesticDog
print("-" * 20)

# Multiple Inheritance
bat = Bat("Bram")
bat.eat()       # Inherited from Animal
bat.hunt()      # Inherited from Predator
bat.flee()      # Inherited from Prey
bat.fly()       # Specific to Bat