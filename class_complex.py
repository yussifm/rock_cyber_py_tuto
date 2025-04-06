
#OOP 
# Encapsulation
# Encapsulation is a way to restrict access to certain attributes and methods of an object

class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # private attribute
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited: ", amount)
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn: ", amount)
        else:
            print("Invalid withdrawal amount")

    def get_balance(self):
        return self.__balance  # public method to access private attribute
    
    
# Create an object of the class
account = BankAccount("123456789", 1000)
account.deposit(500)
print("Current balance: ", account.get_balance())
account.withdraw(200)
print("Current balance: ", account.get_balance())


#Polymorphism
# Polymorphism is the ability to use the same method name for different types of objects

class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    # override the sound method
    def sound(self):
        print("Dog barks")

animal = Animal()
dog = Dog()

print("Animal:")
animal.sound()  # Output: Animal makes a sound
print("Dog:")
dog.sound()  # Output: Dog barks

#abstractions 


