"""
class Human:
    # self is just a convention, you can use any name for it. it refers to this instance of the class
    def __init__(self, name, age):
        self.name = name # basically this name , or whatever we pass when calling.
        self.age = age

    def str(self): # here the self has access to the human self which has name and age with it 
        return "Hi, my name is " + self.name + " and I am " + str(self.age) + " years old."

    def __repr__(self): # the developer-facing form: unambiguous, ideally recreates the object
        return f"Human(name={self.name!r}, age={self.age!r})"

    def greet(self):
        return "Hello, my name is " + self.name + "."

h = Human(age=30, name="Alice")
print(h)  # this will call the __str__ method and print the string representation of the object
print(h.greet())  # this will call the greet method and print the greeting

print("Name:", h.name)  # access the name attribute of the object
print("Age:", h.age)    # access the age attribute of the object

print(h.str())  # this will call the __str__ method and print the string representation of the object 

"""

"""
class Student:
    graduating_year = 2024  # class variable shared by all instances
    num_students = 0  # class variable to keep track of the number of students or objects created in this class

    def __init__(self, name, age):
        self.name = name  # instance variable unique to each instance
        self.age = age    # instance variable unique to each instance
        Student.num_students += 1  # increment the class variable when a new student is created

student1 = Student("Bob", 20) # object creation, this will call the __init__ method and increment the num_students class variable
student2 = Student("Charlie", 22)
student3 = Student("David", 21)

print(f" the graduating year is: {Student.graduating_year}" , f" and the number of students are: {Student.num_students}")  # access the class variable

"""



""""


# Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print (f"{self.name} makes a sound.")
    def eat(self):
        print(f"{self.name} is eating.")

class Dog(Animal):  # Dog class inherits from Animal class
    def speak(self):  # overriding the speak method of Animal class
        print(f"{self.name} barks.")

class cat(Animal):  # Cat class inherits from Animal class
    pass  # no overriding, will use the speak method of Animal class

class mouse(Animal):  # Mouse class inherits from Animal class
    pass


cat1 = cat("Whiskers")
dog1 = Dog("Buddy")
mouse1 = mouse("Jerry")

dog = Dog("Buddy")
Dog.speak(dog)  # Output: Buddy barks. or  ////////////////  dog.speak()  # Output: Buddy barks.



# multiple inheritance - subclass inherits from more than 1 parent class.
class animal:

    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} speaks")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(animal):

    def speak(self):
         print(f"{self.name} barks")

class Cat(animal):

    def speak(self):
        print(f"{self.name} meows")

class DogCat(Dog, Cat):  # DogCat inherits from both Dog and Cat classes
    def speak(self):
        Dog.speak(self)  # call the speak method of Dog class
        Cat.speak(self)  # call the speak method of Cat class

# multilevel inheritance - subclass inherits from a parent class which in turn inherits from another parent class.
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks.")


dooby = Animal("Buddy")
dooby.speak()  # Output: Buddy makes a sound

"""



# Abstract classes - cannot be instantiated, but can be subclassed. They are used to define a common interface for a group of related classes.

"""
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    # we decalre them method but not define it , we will define it in the subclass, this is the main purpose of abstract classes, to define a common interface for a group of related classes.
    
    def go(self):
        pass

    @abstractmethod

    def stop(self):
        pass

class Car(Vehicle):

    def __init__(self):
        self.speed = 0

    def go(self):
        self.speed = 50

    def stop(self):
        self.speed = 0

car = Car()  # This will raise an error because Car does not implement the abstract methods go and stop. so a concrete subclass must implement all abstract methods of the abstract class to be instantiated.

car1 = Car()  # This will work because Car implements the abstract methods go and stop.

car1.go()
print(car1.speed)  # Output: 50

car1.stop()
print(car1.speed)  # Output: 0

"""

"""

# super() function - used to call a method from the parent class. It is used to access methods from a parent class from within a child class.

class shape:
    def __init__(self, color,is_filled):
        self.color = color
        self.is_filled = is_filled

# other shapes may have different ways to get area or anything but color and is_filled is common for all , 
# so we call it using the super function and define the common attributes in the parent class and call it in the child class using the super function.

class rectangle(shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)  # call the __init__ method of the parent class
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class square(shape):

    def __init__(self, color, is_filled, side_length):
        super().__init__(color, is_filled)  # call the __init__ method of the parent class
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2


rectu = rectangle("red", True, 5, 10)
square = square("blue", False, 7)

print(rectu.color)  # Output: red
print(rectu.is_filled)  # Output: True
print(rectu.width)  # Output: 5
print(rectu.height)  # Output: 10
print(rectu.area())  # Output: 50

print(square.color)  # Output: blue
print(square.is_filled)  # Output: False
print(square.side_length)  # Output: 7
print(square.area())  # Output: 49

"""


# Polymorphism- Inheritance and duck typing are two ways to achieve polymorphism in Python. Inheritance allows a subclass to inherit methods and attributes from a parent class, while duck typing allows an object to be treated as an instance of a class if it has the same methods and attributes as that class.

"""

from abc import ABC, abstractmethod

class shape(ABC):

    @abstractmethod
    def area(self):
        pass

class square(shape):

    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

class circle(shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2  


# now suppose we make a pizza class the does not have a area method it only has toppings and radius , but it is a circle. so we inherit the circle class . 
# and because circle was from a shape class , now pizza is also a shape . with area method from circle class.
# so pizza class is both a circle and a shape class. so we can use the area method from the circle class in the pizza class. this is called polymorphism.

class pizza(circle):

    def __init__(self, radius, toppings):
        super().__init__(radius)  # call the __init__ method of the parent class
        self.toppings = toppings

shapes = [square(5), circle(3), pizza(4, ["pepperoni", "mushrooms"])]

for shape in shapes:
    print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")  # Output: The area of the square is: 25, The area of the circle is: 28.26, The area of the pizza is: 50.24

"""


## duck typing - another way to achieve polymorphism besides inheritance
# object must have the minimum necessary attributes or methods to be used in a particular context. if it quacks like a duck, it is a duck. 

"""

class animal:
    alive = True

class dog(animal):
    def speak(self):
        print("Woof!")

class cat(animal):
    def speak(self):
        print("Meow!")

# now dog and cat both have the alive attribute which is not present in car , so we can add that to the car class and make it compatible with the animal class and avoid the attribute error.

class car:
    
    alive = False  # added alive attribute to make it compatible with the animal class

    def speak(self):      # we had horn attribute in car but we change that to speak to make it compatible with the animal class and avoid the attribute error.
        print("Honk!")

animals = [dog(), cat(), car()]

for animal in animals:
    animal.speak()   # Output: Woof!, Meow!, Honk!
    print(animal.alive)  # Output: True, True, False

"""

## Aggregation - a way to combine objects of different classes into a single object. it is a has-a relationship. for example, a car has an engine, a car has wheels, a car has seats, etc. 
# so we can create a car class that has an engine class, a wheel class, and a seat class. this is called aggregation.

"""
class Library:
    def __init__(self, library_name):
        self.library_name = library_name
        self.books = []  # aggregation - a library has books

    def add_book(self, book):
        self.books.append(book)

    def print_books(self):
        for book in self.books:
            return (f"Book title: {book.title}, Author: {book.author}")
        

class Book:
    def __init__(self, Title, Author):
        self.title = Title
        self.author = Author


# creating a function to add books to the library and print them out.


lib = Library(library_name="Dhruv's Library")


book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("To Kill a Mockingbird", "Harper Lee")

lib.add_book(book1)
lib.add_book(book2)


print(f"Library name: {lib.library_name}")  # Output: Library name: My Library

lib.print_books()  # Output: Book title: The Great Gatsby, Author: F. Scott Fitzgerald, Book title: To Kill a Mockingbird, Author: Harper Lee



## composition - a way to combine objects of different classes into a single object. it is a has-a relationship. for example, a car has an engine, a car has wheels, a car has seats, etc.
# so we can create a car class that has an engine class, a wheel class, and

class engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power

class Wheel:
    def __init__(self, size):
        self.size = size

class car:
    def __init__(self, engine, wheels):
        self.engine = engine  # composition - a car has an engine
        self.wheels = wheels  # composition - a car has

"""

# nested classes - a class defined inside another class. it is a way to logically group classes that are only used in one place. it is also a way to encapsulate classes that are only used in one place.

# class methods - a method that is bound to the class and not the instance of the class. it can be called on the class itself or on an instance of the class. it is defined using the @classmethod decorator.

class student:
    school_name = "ABC School"  # class variable

    def __init__(self, name, age):
        self.name = name  # instance variable
        self.age = age    # instance variable

    @classmethod
    def get_school_name(cls):  # class method
        return cls.school_name

print(student.get_school_name())  # Output: ABC School  

