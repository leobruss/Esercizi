#9-1. Restaurant: Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: a restaurant_name and a 
#cuisine_type. Make a method called describe_restaurant() that prints these two pieces of information, and a method called open_restaurant() 
#that prints a message indicating that the restaurant is open. Make an instance called restaurant from your class. Print the two attributes 
#individually, and then call both methods.
class Restaurant:
    def __init__(self, restaurant_name: str, cuisine_type: str) -> None:
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_resturan(self) -> str:
        print(f"Il tipo di cucina servito nel ristorante {self.restaurant_name} è il {self.cuisine_type}")

    def open_resturant(self) ->str:
        print(f"Il ristornate {self.restaurant_name} è aperto")

restaurant = Restaurant("Città d'oriente", "Cinese")
print()
Restaurant.open_resturant(restaurant)
Restaurant.describe_resturan(restaurant)

print("\n")
#9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three different instances from the class, and call describe_restaurant() 
#for each instance.
class Restaurant:
    def __init__(self, restaurant_name: str, cuisine_type: str) -> None:
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_resturan(self) -> str:
        print(f"Il tipo di cucina servito nel ristorante {self.restaurant_name} è il {self.cuisine_type}")

    def open_resturant(self) ->str:
        print(f"Il ristornate {self.restaurant_name} è aperto")

restaurant1 = Restaurant("Città d'oriente", "Cinese")
restaurant2 = Restaurant("Domò", "Giapponese")
restaurant3 = Restaurant("Burger King", "Fast Food")

Restaurant.open_resturant(restaurant1)
Restaurant.describe_resturan(restaurant1)
print()
Restaurant.open_resturant(restaurant2)
Restaurant.describe_resturan(restaurant2)
print()
Restaurant.open_resturant(restaurant3)
Restaurant.describe_resturan(restaurant3)

print("\n")
#9-3. Users: Make a class called User. Create two attributes called first_name and last_name, and then create several other attributes that 
#are typically stored in a user profile. Make a method called describe_user() that prints a summary of the user’s information. Make another 
#method called greet_user() that prints a personalized greeting to the user. Create several instances representing different users, 
#and call both methods for each user.
class User:
    def __init__(self, first_name: str, last_name:str, age: int, gender: str, phone_number: int ) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.phone_number = phone_number

    def describe_user(self) ->str:
        print(f"User information:\nName: {self.first_name}\nSurname; {self.last_name}\nAge: {self.age} anni\nGender: {self.gender}\nPhone number: {self.phone_number}")

    def greet_user(self) ->str:
        print(f"Dear {self.last_name} {self.first_name} thank you for signing up.")

user1 = User("Leonardo", "Brussani", 19, "Male", 3278242560)
user2 = User("Matteo", "Cardelli", 19, "Male", 3298641360)
user3 = User("Gabriela", "Ciuica", 21, "Female", 3278641498)

User.greet_user(user1)
User.describe_user(user1)
print()
User.greet_user(user2)
User.describe_user(user2)
print()
User.greet_user(user3)
User.describe_user(user3)

print("\n")
#9-4. Number Served: Start with your program from Exercise 9-1. Add an attribute called number_served with a default value of 0. 
#Create an instance called restaurant from this class. Print the number of customers the restaurant has served, and then change this value 
#and print it again. Add a method called set_number_served() that lets you set the number of customers that have been served. 
#Call this method with a new number and print the value again. Add a method called increment_number_served() that lets you increment the number 
#of customers who’ve been served. Call this method with any number you like that could represent how many customers were served in, say, a day of business. 
class Restaurant:
    def __init__(self, restaurant_name: str, cuisine_type: str,number_served: int = 0) -> None:
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_resturan(self) -> str:
        print(f"Il tipo di cucina servito nel ristorante {self.restaurant_name} è il {self.cuisine_type} e le persone servite sono {self.number_served}")

    def open_resturant(self) ->str:
        print(f"Il ristornate {self.restaurant_name} è aperto")

    def set_number_served(self, set_number_served: int) -> str:
        self.number_served = set_number_served
        print(f"Il numero di persone servite sono {self.number_served}")
        
    
    def increment_number_served(self, increment_number_served: int) -> str:
        self.number_served += increment_number_served
        print(f"Il numero di persone incrementato che sono state servite sono {self.number_served}")

restaurant = Restaurant("Città d'oriente", "Cinese", 3)
print()
restaurant.open_resturant()
restaurant.describe_resturan()
print()

restaurant.set_number_served(4)
restaurant.increment_number_served(2)

print("\n")
#9-5. Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3. Write a method called increment_login_attempts() 
#that increments the value of login_attempts by 1. Write another method called reset_login_attempts() that resets the value of login_attempts to 0. 
#Make an instance of the User class and call increment_login_attempts() several times. Print the value of login_attempts to make sure it was incremented 
#properly, and then call reset_login_attempts(). Print login_attempts again to make sure it was reset to 0.
class User:
    def __init__(self, first_name: str, last_name:str, age: int, gender: str, phone_number: int, login_attempts: int) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.phone_number = phone_number
        self.login_attempts = login_attempts

    def describe_user(self) ->str:
        print(f"User information:\nName: {self.first_name}\nSurname; {self.last_name}\nAge: {self.age} anni\nGender: {self.gender}\nPhone number: {self.phone_number}\nLogin attempts: {self.login_attempts}")

    def greet_user(self) ->str:
        print(f"Dear {self.last_name} {self.first_name} thank you for signing up.")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print("The value of login attempts is reset in 0")
        print(f"User information:\nName: {self.first_name}\nSurname; {self.last_name}\nAge: {self.age} anni\nGender: {self.gender}\nPhone number: {self.phone_number}\nLogin attempts: {self.login_attempts}")


user1 = User("Leonardo", "Brussani", 19, "Male", 3278242560, 1)
user2 = User("Matteo", "Cardelli", 19, "Male", 3298641360, 1)
user3 = User("Gabriela", "Ciuica", 21, "Female", 3278641498, 2)

user1.greet_user()
user1.describe_user()
print()
user1.reset_login_attempts()
print()
user2.greet_user()
user2.describe_user()
print()
user2.reset_login_attempts()
print()
user3.greet_user()
user3.describe_user()
print()
user3.reset_login_attempts()

print("\n")
#9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write a class called IceCreamStand that inherits from the Restaurant 
#class you wrote in Exercise 9-1  or Exercise 9-4. Either version of the class will work; just pick the one you like better. 
#Add an attribute called flavors that stores a list of ice cream flavors. Write a method that displays these flavors. 
#Create an instance of IceCreamStand, and call this method. 
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name: str, cuisine_type: str, number_served: int = 0, flavors: list = []) -> None:
        super().__init__(restaurant_name, cuisine_type, number_served)
        self.flavors = flavors    
        print(f"Il tipo di cucina servito nel ristorante {self.restaurant_name} è una {self.cuisine_type}\nIl menù è:\n{', '.join(self.flavors)}\nLe persone servite sono {self.number_served}")

restaurant = IceCreamStand("IceCreamStand", "Gelateria", 5, ["Cioccolato", "Vaniglia", "Pistacchio", "Pannna", "Crema", "Fragola"])

print("\n")
#9-7. Admin: An administrator is a special kind of user. Write a class called Admin that inherits from the User class you wrote in 
#Exercise 9-3 or Exercise 9-5. Add an attribute, privileges, that stores a list of strings like "can add post", "can delete post", "can ban user", 
#and so on. Write a method called show_privileges() that lists the administrator’s set of privileges. Create an instance of Admin, and call your method. 
class Admin(User):
    def __init__(self, first_name: str, last_name: str, age: int, gender: str, phone_number: int, login_attempts: int, privileges: list = []) -> None:
        super().__init__(first_name, last_name, age, gender, phone_number, login_attempts)
        self.privileges = privileges

    def show_privileges(self) -> list:
        print(f"The privileges of {self.last_name} {self.first_name} are:\n{', '.join(self.privileges)}")

user1 = Admin("Leonardo", "Brussani", 19, "Male", 3278242560, 1, ["can add post", "can delete post", "can ban user"])
user1.show_privileges()

print("\n")
#9-8. Privileges: Write a separate Privileges class. The class should have one attribute, privileges, that stores a list of strings as described 
#in Exercise 9-7. Move the show_privileges() method to this class. Make a Privileges instance as an attribute in the Admin class. 
#Create a new instance of Admin and use your method to show its privileges.
class Admin(User):
    def __init__(self, first_name: str, last_name: str, age: int, gender: str, phone_number: int, login_attempts: int, privileges: list = []) -> None:
        super().__init__(first_name, last_name, age, gender, phone_number, login_attempts)
        self.privileges = privileges

        
class Privileges:
    def __init__(self, privileges) -> None:
        self.privileges = privileges

    def show_privileges(self) -> list:
        print(f"The privileges of {self.last_name} {self.first_name} are:\n{', '.join(self.privileges)}")

user1 = Admin("Leonardo", "Brussani", 19, "Male", 3278242560, 1, ["can add post", "can delete post", "can ban user"])
Privileges.show_privileges(user1)

print("\n")
#9-9. Battery Upgrade: Use the final version of electric_car.py from this section. Add a method to the Battery class called upgrade_battery(). 
#This method should check the battery size and set the capacity to 65 if it isn’t already. Make an electric car with a default battery size, 
#call get_range() once, and then call get_range() a second time after upgrading the battery. You should see an increase in the car’s range.

#9-10. Imported Restaurant: Using your latest Restaurant class, store it in a module. Make a separate file that imports Restaurant. 
#Make a Restaurant instance, and call one of Restaurant’s methods to show that the import statement is working properly.

#DONE

#9-11. Imported Admin: Start with your work from Exercise 9-8. Store the classes User, Privileges, and Admin in one module. 
#Create a separate file, make an Admin instance, and call show_privileges() to show that everything is working correctly.

#Done

#9-12. Multiple Modules: Store the User class in one module, and store the Privileges and Admin classes in a separate module. In a separate file, 
#create an Admin instance and call show_privileges() to show that everything is still working correctly.

#9-13. Dice: Make a class Die with one attribute called sides, which has a default value of 6. Write a method called roll_die() that prints a 
#random number between 1 and the number of sides the die has. Make a 6-sided die and roll it 10 times. Make a 10-sided die and a 20-sided die. 
#Roll each die 10 times.
from random import randint
class Die:
    def __init__(self, sides: int = 6) -> None:
        self.sides = sides

    def roll_die(self ) -> None:
        x = randint(1, self.sides)
        while True:
            



#9-14. Lottery: Make a list or tuple containing a series of 10 numbers and 5 letters. Randomly select 4 numbers or letters from the list and print 
#a message saying that any ticket matching these 4 numbers or letters wins a prize.

#9-15. Lottery Analysis: You can use a loop to see how hard it might be to win the kind of lottery you just modeled. Make a list or tuple called 
#my_ticket. Write a loop that keeps pulling numbers until your ticket wins. Print a message reporting how many times the loop had to run to give 
#you a winning ticket.