# Basics

print("Hello world")

#int age = 5;
age = 5
salary = 100000.5555

name = "John Doe"

male = True
female = False

#Control flow
# Conditional Statements that allows your program to make decisions based on certain conditions.
number = 5

#Keyword : if, elif, else
name = "Ama"
if name == "Ama":
    print("Hello Ama")
else:
    print("Hello Coded")

if number > 0:
    #code block or block of code
    print("Positive")
    
    #Else if
elif number < 0:
    print("Negative")
else:
    print("Zero")

# Loops
fruits = ["apple", "banana", "cherry"] # List of strings (fruits)
listOfNumbers = [1, 2, 3, 4, 5] # List of integers (numbers)

for Damascus in fruits:
    if Damascus == "banana":
        break # Break the loop if fruit is banana
    print(f"I love: {Damascus}")
    print("I love: " + Damascus)
    print("I love: ", Damascus)

#While loop
counter = 5
while counter > 0:
    print("Counter is: ", counter)
    #
    counter -= 1 # Decrement counter by 1
    #counter = counter - 1 # Decrement counter by 1
    

#Functions
# void function
# Keyword : def ->  helps to define a function
# function_name(parameters) -> function signature
#int add(int a, int b){}  --> C++ example 
def greet(name: str):
    print("Hello, " + name + "!")

def add(a: int, b: int) -> int:
    return a + b  # statement

def multiple(a, b):
    return a * b

# Slop function
def slop_of_curve(x1,x2, y1, y2):
    return (y1 - y2) / (x1 - x2)


slop_of_curve(1, 2, 3, 4) # function call
#Anonymous function (lambda function)
# lambda a, b: a + b
x = lambda a: a+ 10
add = lambda a, b: a + b
multiple = lambda a, b: a * b
print(x(5)) 
print(add(5, 10))
print(multiple(5, 10))

#Function call
greet("Alice")
greet("AMA")

addition = add(5, 10)
print("Addition is: ", addition)

multiplication = multiple(5, 10)
print("Multiple is: ", multiplication)

# Data Structures
# List
colors = ["red", "green", "blue",] # list start with 0
first_element = colors[0] # first element
print("First element is: ", first_element)
print("Colors are: ", colors)
print("Length of colors: ", len(colors))
colors.append("peach")
colors.append("white")
colors.append("black")

print("Colors are: ", colors)
print("Length of colors: ", len(colors))

#Tuples 
# Immutable list
# Tuple is a collection of ordered elements
dimensions = (1080, 720)


#Dictionary
# Key-value pairs
# Dictionary is a collection of key-value pairs
person = {
    "name": "AMA",
    "age": 25,
    "city": "New York",
    "occupation": "Engineer"
}

person.update({"name": "John Doe"})
print("Person is: ", person)
print("Person name is: ", person["name"])

#Sets 
# Unordered collection of unique elements
# Set is a collection of unique elements
unique_numbers = {1, 2, 3, 4, 5, 5}
print("Unique numbers are: ", unique_numbers)


list_of_dict = [
    {"name": "John", "age": 30},
    {"name": "Jane", "age": 25},
    {"name": "Doe", "age": 35}
]
print("List of dict is: ", list_of_dict)
print("first value of first index: ", list_of_dict[0]["name"])



# File Handling I/O
# Open a file in write mode
with open("example.docx", "w") as file:
    for i in range(1000):
        file.write("I will never talk to a Girl in Class\n")
    file.write("Hello, World!\n")
    file.write("This is a test file.\n")
    file.write("Rock Cyber Elite\n")
    file.write("Rock Cyber Elite")
    file.write("Rock Cyber Elite")
    
    
# Open a file in read mode
with open("spams.txt", "r") as file:
    # Read the entire file
    content = file.read()
    #print(content)


# Exception Handling
# try, except, finally
try:
    # code that may raise an exception
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError as e:
    # handle the exception
    print("Error: Division by zero!")
    print(e)
# finally:
#     # code that will always execute
#     print("This will always execute.")


# Classes and Objects -> OOP => Object Oriented Programming
 # class : blueprint of an object
# object : instance of a class
# attribute : property / variable of an object
# method : function defined inside a class

class Person:
    # constructor -> a special method that is called when an object is created
    def __init__(self, name, age, occupation):
        # self is a reference to the current object / current instance of the class
        self.name = name  # attribute
        self.age = age  # attribute
        self.occupation = occupation  # attribute

    # method
    def greet(self):
        print("Hello, my name is " + self.name + ", I am " + str(self.age) + " years old, and I work as a " + self.occupation + ".")


# Create an object of the class
person1 = Person("John Doe", 30, "Engineer")
alice = Person("Alice", 25, "Doctor")
Ama = Person("AMA", 25, "Engineer")

# Call the method of the object
person1.greet()
alice.greet()
Ama.greet()


# Inheritance
# Inheritance is a way to create a new class from an existing class

class Student(Person):
    def __init__(self, name, age, occupation, student_id):
        # Call the constructor of the parent class
        # super() is used to call the constructor of the parent class
        # super() returns a temporary object of the superclass
        super().__init__(name, age, occupation)  # Call the constructor of the parent class
        self.student_id = student_id  # attribute

    def study(self):
        print("I am studying.")
    def greet(self):
        print("Hello, my name is " + self.name + ", I am " + str(self.age) + " years old, and I am a student with ID " + self.student_id + ".")
        
    def display_student_info(self):
        print("Student ID: ", self.student_id)
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Occupation: ", self.occupation)

# Create an object of the Student class
student1 = Student("Coded", 25, "Doctor", "S12345")
student1.greet()  # Call the method of the parent class
student1.study()  # Call the method of the child class
student1.display_student_info()  # Call the method of the child class

