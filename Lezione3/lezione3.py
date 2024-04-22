#4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of each pizza.
#• Modify your for loop to print a sentence using the name of the pizza, instead of printing just the name of the pizza. For each pizza, you should have one line 
#of output containing a simple statement like I like pepperoni pizza.
#• Add a line at the end of your program, outside the for loop, that states how much you like pizza. The output should consist of three or more lines about the kinds 
#of pizza you like and then an additional sentence, such as I really love pizza!

pizzas: list = ["Margerita", "4 Formaggi", "Crostino"]

for pizza in pizzas :
    print("I like", pizza,".")

print()
print(f"{pizzas[0]} is my favorite pizza.\nMy father love {pizzas[1]} pizza.\n{pizzas[2]} is my second favourite pizza.")
print("\n")



#4-2. Animals: Think of at least three different animals that have a common characteristic. Store the names of these animals in a list, and then use a for loop to 
#print out the name of each animal.
#• Modify your program to print a statement about each animal, such as A dog would make a great pet.
#• Add a line at the end of your program, stating what these animals have in common. You could print a sentence, such as Any of these animals would make a great pet!
animals: list = ["Lion", "Elephant", "Giraffe"]
statement: list = ["is the king of Savannah", "is a realy big animal", "has a really long neck"]
for a, s in zip(animals, statement):
    print(a,s)
    
print("\n")



#4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.
for x in range(1, 21):
    print(x)
print("\n") 



#4-4. One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers. (If the output is taking too long, stop it by 
#pressing CTRL-C or by closing the output window.)
yes = input("Do you want to print one milion numbers(Y/N) ")
yes = yes.upper()
if yes == "Y":
    
    number: list = []
    for x in range(1, 1000001):
        number.append(x)
    for x in number:
        print(x)
    print("\n") 



#4-5. Summing a Million: Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and ends at 
#one million. Also, use the sum() function to see how quickly Python can add a million numbers.

number: list = []
for x in range(1, 1000001):
    number.append(x)

print(min(number))
print(max(number))
print(sum(number))
print("\n") 



#4-6. Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number.

odd_numbers: list = list(range(1, 21, 2))
for n in odd_numbers:
    print(n)
print("\n")



#4-7. Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop to print the numbers in your list.
multiples_of3: list = list(range(3, 31, 3))
for n in multiples_of3:
    print(n)
print("\n")



#4-8. Cubes: A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes 
#(that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube.
cube: list = list(range(1,11))
for n in cube:
    print(n**3)
    
print("\n")



#4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.
cube: list = [n**3 for n in range(1,11)]
for n in cube :
    print(n)





#4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
#• Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
#• Print the message Three items from the middle of the list are:. Then use a slice to print three items from the middle of the list.
#• Print the message The last three items in the list are:. Then use a slice to print the last three items in the list.
animals: list = ["Lion", "Elephant", "Giraffe", "Tiger", "Bird"]

print(f"The first three items in the list are : {animals[:3]}.")
print(f"Three items from the middle of the list are: {animals[1:4]}.")
print(f"The last three items in the list are: {animals[-3:]}.")

print("\n")




#4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1. Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
#• Add a new pizza to the original list.
#• Add a different pizza to the list friend_pizzas.
#• Prove that you have two separate lists. Print the message My favorite pizzas are:, and then use a for loop to print the first list. 
#Print the message My friend’s favorite pizzas are:, and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.

pizzas: list = ["Margerita", "4 Formaggi", "Crostino"]
friend_pizzas: list = ["Margerita", "4 Formaggi", "Crostino"]
pizzas.append("Diavola")
friend_pizzas.append("Boscaiola")

for p in pizzas :
    message: str = f"My favorite pizzas are : {p}" 
    print(message)

print()

for fp in friend_pizzas :
    message: str = f"My friend's favorite pizzas are: {fp}"
    print(message)

print("\n")



#4-12. More Loops: All versions of foods.py in this section have avoided using for loops when printing, to save space.
#Choose a version of foods.py, and write two for loops to print each list of foods.

#Done in exercise 4-11


#4-14. PEP 8: Look through the original PEP 8 style guide at https://python.org/dev/peps/pep-0008. You won’t use much of it now, 
#but it might be interesting to skim through it.

#Done

#4-15. Code Review: Choose three of the programs you’ve written in this chapter and modify each one to comply with PEP 8.

#Done

#5-1. Conditional Tests: Write a series of conditional tests. Print a statement
#describing each test and your prediction for the results of each test. Your code
#should look something like this:
#car = 'subaru'
#print("Is car == 'subaru'? I predict True.")
#print(car == 'subaru')
#print("\nIs car == 'audi'? I predict False.")
#print(car == 'audi')
#• Look closely at your results, and make sure you understand why each line evaluates to True or False.
#• Create at least 10 tests. Have at least 5 tests evaluate to True and another 5 tests evaluate to False.
car = 'subaru'
color_car = 'blue'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
print("\nIs car == 'porsche'? I predict False.")
print(car == 'porsche')
print("\nIs car == 'lamborghini'? I predict False.")
print(car == 'lamborghini')
print("\nIs car == 'mustang'? I predict False.")
print(car == 'mustang')
print("\nIs color_car == 'red'? I predict False.")
print(color_car == 'red')
print("\nIs color_car == 'green'? I predict False.")
print(color_car == 'green')
print("\nIs color_car == 'blue'? I predict True.")
print(color_car == 'blue')
print("\nIs color_car == 'pink'? I predict False.")
print(color_car == 'pink')
print("\nIs color_car == 'black'? I predict False.")
print(color_car == 'black')



#5-2. More Conditional Tests: You don’t have to limit the number of tests you 
# create to 10. If you want to try more comparisons, write more tests and add them
#to conditional_tests.py. Have at least one True and one False result for each of
#the following:
#• Tests for equality and inequality with strings
#• Tests using the lower() method
#• Numerical tests involving equality and inequality, greater than and less
#than, greater than or equal to, and less than or equal to
#• Tests using the and keyword and the or keyword
#• Test whether an item is in a list
#• Test whether an item is not in a list
# Tests for equality and inequality with strings
car = 'Toyota'
bike = 'Honda'
print("Is car brand Toyota? True")
print(car == 'Toyota')
print("Is bike brand Toyota? False")
print(bike == 'Toyota')
print()
# Tests using the lower() method
username = 'Leobruss'
print("Is username admin? True")
print(username.lower() == 'leobruss')
print("Is username guest? False")
print(username.lower() == 'admin')
print()
# Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to
number = 35
print("Is number equal to 35? True")
print(number == 35)
print("Is number not equal to 99? True")
print(number != 99)
print("Is number greater than 50? False")
print(number > 50)
print("Is number less than or equal to 35? True")
print(number <= 35)
print()
# Tests using the and keyword and the or keyword
age = 20
print("Is age between 20 and 30? True")
print(age >= 20 and age <= 30)
print("Is age less than 18 or greater than 65? False")
print(age < 18 or age > 65)
print()
# Test whether an item is in a list
fruits = ['apple', 'banana', 'orange']
print("Is 'apple' in the list? True")
print('apple' in fruits)
print("Is 'grape' in the list? False")
print('grape' in fruits)
print()
# Test whether an item is not in a list
cars = ['Toyota', 'Honda', 'Ford']
print("Is 'Tesla' not in the list? True")
print('Tesla' not in cars)
print("Is 'Honda' not in the list? False")
print('Honda' not in cars)
print("\n")



#5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
#• Write an if statement to test whether the alien’s color is green. If it is, print a message that the player just earned 5 points.
#• Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)
alien_color = "green"
if alien_color == "green":
    print("You earned 5 points") 
alien_color = "yellow"
if alien_color == "red":
    print()
print()



#5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.
#• If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
#• If the alien’s color isn’t green, print a statement that the player just earned 10 points.
#• Write one version of this program that runs the if block and another that runs the else block.
alien_color = "green"
if alien_color == "green":
    print("You earned 5 points") 
else:
     print("You earned 10 points") 
print()
alien_color = "red"
if alien_color == "green":
    print("You earned 5 points") 
else:
     print("You earned 10 points") 

print("\n")

#5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.

#• If the alien is green, print a message that the player earned 5 points.
#• If the alien is yellow, print a message that the player earned 10 points.
#• If the alien is red, print a message that the player earned 15 points.
#• Write three versions of this program, making sure each message is printed for the appropriate color alien.
alien_color = "green"
if alien_color == "green":
    print("You earned 5 points") 
elif alien_color == "yellow" :
     print("You earned 10 points") 
else :
     print("You earned 15 points") 
print()
alien_color = "yellow"
if alien_color == "green":
    print("You earned 5 points") 
elif alien_color == "yellow" :
     print("You earned 10 points") 
else:
     print("You earned 15 points")
print()
alien_color = "red"
if alien_color == "green":
    print("You earned 5 points") 
elif alien_color == "yellow" :
     print("You earned 10 points") 
else:
     print("You earned 15 points")

print("\n")



#5-6. Stages of Life: Write an if-elif-else chain that determines a person’s stage of life. Set a value for the variable age, and then:
#• If the person is less than 2 years old, print a message that the person is a baby.
#• If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
#• If the person is at least 4 years old but less than 13, print a message that the person is a kid.
#• If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
#• If the person is at least 20 years old but less than 65, print a message that the person is an adult.
#• If the person is age 65 or older, print a message that the person is an elder.
age = int(input("Enter your age :"))
if age < 2 :
    print("You are a baby")
elif age >= 2 and age <4 :
    print("You are a toddler")
elif age >= 4 and age <13 :
    print("You are a kid")
elif age >= 13 and age <20 :
    print("You are a teenager")
elif age >= 20 and age <65 :
    print("You are a adult")
elif age >= 65 :
    print("You are a elder")

print("\n")



#5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list.
#• Make a list of your three favorite fruits and call it favorite_fruits.
#• Write five if statements. Each should check whether a certain kind of fruit is in your list. If the fruit is in your list, the if block should print a statement, such as You really like Apples!
favorite_fruits: list = ["watermelon", "coconut", "cherries"]
if  f"{favorite_fruits[0]}":
    print("You really like watermelon!")
if favorite_fruits == "apple":
    print("You really like apple!")
if f"{favorite_fruits[1]}":
    print("You really like coconut!")
if favorite_fruits == "banana":
    print("You really like banana!")
if f"{favorite_fruits[2]}":
    print("You really like cherries!")
print("\n")



#5-8. Hello Admin: Make a list of five or more usernames, including the name 'admin'. Imagine you are writing code that will print a greeting to each user after they log in to a website. 
# Loop through the list, and print a greeting to each user.
#• If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
#• Otherwise, print a generic greeting, such as Hello Jaden, thank you for logging in again.
usernames: list = [ "1234", "qwerty", "username", "admin", "guest"]
for greating in usernames:
    if greating == "admin":
        print("Hello admin , would you like to see a status report?\n")
    else:
        print(f"Hello {greating} thank you for logging in again.\n")

print("\n")



#5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is not empty.
#• If the list is empty, print the message We need to find some users!
#• Remove all of the usernames from your list, and make sure the correct message is printed.
usernames: list = [ "1234", "qwerty", "username", "admin", "guest"]
if len(usernames) == 0:
    print("We need to find some users!")
for greating in usernames:
    if greating == "admin":
        print("Hello admin , would you like to see a status report?\n")
    else:
        print(f"Hello {greating} thank you for logging in again.\n")

print("\n")



#5-10. Checking Usernames: Do the following to create a program that simulates how websites ensure that everyone has a unique username.
#• Make a list of five or more usernames called current_users.
#• Make another list of five usernames called new_users. Make sure one or two of the new usernames are also in the current_users list.
#• Loop through the new_users list to see if each new username has already been used. If it has, print a message that the person will need to enter a new username. If a username has not been 
# used, print a message saying that the username is available.
#• Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted. (To do this, you’ll need to make a copy of current_users containing the lowercase 
# versions of all existing users.)
current_users: list = ["1234", "qwerty", "username", "admin", "guest"]
new_users: list = ["admin", "Leonardo", "guest", "Matteo123", "ForzaWarriors"]
for nu in new_users:
    if nu in current_users: 
        print(f"Sorry, the username '{nu}' is already taken. Please enter a new username.")
    else:
        print(f"The username '{nu}' is available.")

print("\n")



#5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
#• Store the numbers 1 through 9 in a list.
#• Loop through the list.
#• Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number. Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a separate line.
number: list = list(range(1,10))
for ordinal in number:
    if ordinal == 1:
        print(f"{ordinal}st")
    elif ordinal == 2:
        print(f"{ordinal}nd")
    elif ordinal == 3:
        print(f"{ordinal}rd")
    else:
        print(f"{ordinal}th")
