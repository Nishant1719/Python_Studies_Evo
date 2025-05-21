# name = "Waghade" # This is a global variable.
# class Car:
#     # name = 123 # This is a class variable.
#     # Always use capitalized letters for class names.
#     def __init__(self, brand, model): # Attribute constructor.
#         # Use self to refer to instance variables.
#         self.__brand = brand # # This is an Private instance variable. # Encapsulation
#         self.model = model # This is an instance variable.
#     # Private Instance variable can be accessed within the class but not outside the class in inherited classes also.
#     def get_brand(self):
#         return self.__brand
    
#     def fullname(self):
#         return print(f"{self.__brand} {self.model}")
    
    
#     def cap(self):
#         if isinstance(self.__brand, str):
#             self.__brand = self.__brand.upper()
#         else:
#             print("Name is not Valid")
            
#     def display(self):
#         return print(f"Name : {self.__brand}")

#For Setter method :
class Car:
    __total_car = 0
    def __init__(self,model): 
        self.__brand = None # This is an Private instance variable. # Encapsulation
        self.model = model
        Car.__total_car += 1
         
    def set_brand(self,value): # Encapsulation
        self.__brand = value
        return
    
    def get_brand(self): # Encapsulation
        return self.__brand
    
    def fullname(self):
        return print(f"{self.__brand} {self.model}")
    
    def cap(self):
        if isinstance(self.__brand, str):
            self.__brand = self.__brand.upper()
        else:
            print("Name is not Valid")
            
    def display(self):
        return print(f"Name : {self.__brand}")    
    
    def fuel_type(self):
        return print("Petrol Or Diesel")

    @staticmethod
    def general_description():
        return print(f"This is a car obj static method & Obj Counts are {Car.__total_car}")
 
# myObj = Car("Merc","Maybach") # Create an instance of MyClass.
# print(myObj.__brand) # Output: Merc
# print(myObj.model) # Output: Maybach
# myObj.cap()
# myObj.display() # 

# Inheritance
# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand, model)
#         self.battery_size = battery_size

# my_BE6 = ElectricCar("Mahindra", "BE6", "65KW")
# print(my_BE6.__brand) # Throws an error because __brand is a private instance variable. # Encapsulation
# Setter :
class ElectricCar(Car):
    def __init__(self, model, battery_size):
        super().__init__(model)
        self.battery_size = battery_size
        
    def fuel_type(self):
        return print("Electricity")
        
my_BE6 = ElectricCar("BE6", "65KW")
print(my_BE6.model)
print(my_BE6.battery_size)
my_BE6.set_brand("Mahindra") # Encapsulation
# print(my_BE6.get_brand()) # Accessing the private instance variable using the getter method. # Encapsulation
my_BE6.fullname() 
# my_BE6.fuel_type() # # Polymorphism Example

XUV700 = Car("XUV") # Polymorphism Example
XUV700.fuel_type() # # Polymorphism Example

Car.general_description() # Static Method Example
XUV700.general_description() # Static Method Example 



# Static Method:
# Defination: A static method belongs to the class rather than an instance of the class.
# - It can be called on the class itself, or on an instance of the class.
# - It does not require an instance of the class to be created.
# - It does not have access to the instance (self) or class (cls) variables.
# - It is used to perform a task that is related to the class but does not require access to instance or class variables.
# - It is defined using the @staticmethod decorator.
    # Usage:
        # It is used when you want to define a method that does not require access to instance or class variables.
# class Car:
#     total_car = 0
#     def __init__(self, model):
#         self.__brand = None
#         self.model = model
#         Car.total_car += 1

#     @staticmethod
#     def get_total_cars():
#         return Car.total_car

# Property Decorators :
    # - Property decorators are used to define getter and setter methods for instance variables.
    # - They allow you to access and modify instance variables in a controlled way.
        # Example:
        # class Car:
        #     def __init__(self, model):
        #         self.__brand = None
        #         self.model = model

        #     @property
        #     def brand(self):
        #         return self.__brand

        #     @brand.setter
        #     def brand(self, value):
        #         self.__brand = value
        
        #     @brand.deleter
        #     def brand(self):
        #         del self.__brand
# Usage :
# my_car = Car("Model S")
# my_car.brand = "Tesla"        # Setter is called
# print(my_car.brand)           # Getter is called: Output -> Tesla
# del my_car.brand              # Deleter is called
# print(my_car.brand)           # Will raise AttributeError because __brand is deleted

# Practice :
class MyGames:
    def __init__(self):
        self.__games = None
    
    @property
    def game(self):
        return self.__games

    @game.setter
    def set_game(self,value):
        self.__games = value
        
    @game.deleter
    def del_game(self):
        self.__games = None 

new_games = MyGames()
new_games.set_game = "GTA5"
print(new_games.game)

MyGames.set_game = "PUBG" # This will not work because set_game is an instance variable, not a class variable.
print(new_games.game) # Output: PUBG


# Notes:
# 1. Class variables are shared across all instances of the class.
    # - Meaning : If you change the class variable, it will change for all instances.
# 2. Instance variables are unique to each instance of the class.
    # - Meaning : If you change the instance variable in one instance, it won't affect the other instances.
# 3. Property decorators are primarily used for instance variables.

# Important URL: https://www.youtube.com/watch?v=6soT3DMBJGQ&list=PLu71SKxNbfoBsMugTFALhdLlZ5VOqCg2s&index=18
    # Static methods, OOPs Concepts