#Leonardo Bruassani 
#17/04/2024

import random


print("Hello Wolrd")
print("\n")

#2-3. Personal Message: Use a variable to represent a person’s name, and print a message to that person. 
#Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”
name: str = "Eric"
message: str = f"Hello {name}, woul you like to learn som Python today?"
print(message)
print("\n")



#2-4. Name Cases: Use a variable to represent a person’s name, and then print that person’s name in lowercase, 
#uppercase, and title case.
name: str = "Eric"
print(name.lower())
print(name.upper())
print(name.title())
print("\n")


#2-5. Famous Quote: Find a quote from a famous person you admire. Print the quote and the name of its author. 
#Your output should look something like the following, including the quotation marks: Albert Einstein once said, 
#“A person who never made a mistake never tried anything new.”
author_name: str =  "Sean Connery"
quote: str = "I'm Bond, James Bond"
print(f"{author_name} during the 007 movie said : \"{quote}\"")
print("\n")


#2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the famous person’s name using a variable called famous_person. 
#Then compose your message and represent it with a new variable called message. Print your message. 
author_name: str =  "Sean Connery"
quote: str = "I'm Bond, James Bond"
print(f"{author_name} during the 007 movie said : \"{quote}\"")
print("\n")


#2-8. File Extensions: Python has a removesuffix() method that works exactly like removeprefix(). 
#Assign the value 'python_notes.txt' to a variable called filename. Then use the removesuffix() 
#method to display the filename without the file extension, like some file browsers do.
filename: str = 'python_notes.txt'
message = filename.removesuffix(".txt")
print(message)
print("\n")


#3-1. Names: Store the names of a few of your friends in a list called names. Print each person’s name by accessing each element in the list, one at a time.
names: list = ["Matteo", "Bruno", "Lorenzo", "Alessandro", "Giovanni"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])
print("\n")


#3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them. 
#The text of each message should be the same, but each message should be personalized with the person’s name.
names: list = ["Matteo", "Bruno", "Lorenzo", "Alessandro", "Giovanni"]
message = f"Hi {names[0]}, how are you?"
print(message)
message = f"Hi {names[1]}, how are you?"
print(message)
message = f"Hi {names[2]}, how are you?"
print(message)
message = f"Hi {names[3]}, how are you?"
print(message)
message = f"Hi {names[4]}, how are you?"
print(message)
print("\n")


#3-3. Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. 
#Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”
cars: list = ["718 Cayman GT4 RS", "Chevrolet Camaro 2.0", "Lamborghini AVENTADOR S ROADSTER"]
message = f"{cars[0]} is one of my favorite models but unfortunately it costs too much."
print(message)
message = f"{cars[1]} is an excellent machine and with a more affordable price."
print(message)
message = f"{cars[2]} is simply a dream."
print(message)
print("\n")


#3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three 
#people you’d like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.
names: list = ["Davide", "William", "Giorgio"]
message = f"{names[0]} you were invited to dinner with me."
print(message)
message = f"{names[1]} you were invited to dinner with me."
print(message)
message = f"{names[2]} you were invited to dinner with me."
print(message)
print("\n")


#3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. 
#You’ll have to think of someone else to invite.
#• Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it.
#• Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
#• Print a second set of invitation messages, one for each person who is still in your list.
names: list = ["Davide", "William", "Giorgio"]
names.insert(2,"Guido")
message = f"{names[0]} you were invited to dinner with me."
print(message)
message = f"{names[1]} you were invited to dinner with me."
print(message)
message = f"{names[2]} you were invited to dinner with me."
print(message)
print("\n")


#3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
#• Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
#• Use insert() to add one new guest to the beginning of your list.
#• Use insert() to add one new guest to the middle of your list.
#• Use append() to add one new guest to the end of your list.
#• Print a new set of invitation messages, one for each person in your list.

names: list = ["Davide", "William", "Giorgio"]
names.insert(0,"Mirko")
names.insert(2,"Guido")
names.insert(5,"Pierfrancesco")
message = f"{names[0]} you were invited to dinner with me."
print(message)
message = f"{names[1]} you were invited to dinner with me."
print(message)
message = f"{names[2]} you were invited to dinner with me."
print(message)
message = f"{names[3]} you were invited to dinner with me."
print(message)
message = f"{names[4]} you were invited to dinner with me."
print(message)
message = f"{names[5]} you were invited to dinner with me."
print(message)
message = "I invited you all since i found a bigger table."
print (message)
print("\n")


#3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.
#• Start with your program from Exercise 3-6. 
#Add a new line that prints a message saying that you can invite only two people for dinner.
#• Use pop() to remove guests from your list one at a time until only two names remain in your list. 
#Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
#• Print a message to each of the two people still on your list, letting them know they’re still invited.
#• Use del to remove the last two names from your list, so you have an empty list. 
#Print your list to make sure you actually have an empty list at the end of your program.
names: list = ["Mirko", "Davide", "Guido", "William", "Giorgio", "Pierfrancesco"]
message = "I'm so sorry, but today i can invite only 2 person."
print(message)

message = f"I'm sorry {names[0]} but you can't come tonight."
print(message)
names.pop(0)

message = f"I'm sorry {names[1]} but you can't come tonight."
print(message)
names.pop(1)

message = f"I'm sorry {names[2]} but you can't come tonight."
print(message)
names.pop(2)

message = f"I'm sorry {names[2]} but you can't come tonight."
print(message)
names.pop(2)

message = f"Hi {names[0]} i invite you to dinner with me."
print(message)

message = f"Hi {names[1]} i invite you to dinner with me."
print(message)

del names[:]
print(names)
print("\n")


#3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
#• Store the locations in a list. Make sure the list is not in alphabetical order.
#• Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
#• Use sorted() to print your list in alphabetical order without modifying the actual list.
#• Show that your list is still in its original order by printing it.
#• Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
#• Show that your list is still in its original order by printing it again.
#• Use reverse()  to change the order of your list. Print the list to show that its order has changed.
#• Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
#• Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
#• Use sort() to change your list so it’s stored in reverse-alphabetical order.
#Print the list to show that its order has changed.
place: list = ["japan", "Bali", "San Francisco", "Singapore", "Miami"]
print(place)

alphabetical_order: list = sorted(place)
print(alphabetical_order)

alphabetical_order: list = sorted(place, reverse=True)
print(alphabetical_order)

place.reverse()
print(place)

place.reverse()
print(place)

place.sort()
print(place)

place.sort(reverse=True)
print(place)
print("\n")


#3-9. Dinner Guests: Working with one of the programs 
#from Exercises 3, use len() to print a message indicating the number of people you’re inviting to dinner.
names: list = ["Davide", "William", "Giorgio"]
names.insert(0,"Mirko")
names.insert(2,"Guido")
names.insert(5,"Pierfrancesco")
message = f"{names[0]} you were invited to dinner with me."
print(message)
message = f"{names[1]} you were invited to dinner with me."
print(message)
message = f"{names[2]} you were invited to dinner with me."
print(message)
message = f"{names[3]} you were invited to dinner with me."
print(message)
message = f"{names[4]} you were invited to dinner with me."
print(message)
message = f"{names[5]} you were invited to dinner with me."
print(message)
message = "I invited you all since i found a bigger table."
print (message)

lenght = len(names)
print(lenght)
print("\n")


#6-1. Person: Use a dictionary to store information about a person you know. 
#Store their first name, last name, age, and the city in which they live. 
#You should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.
person: dict = {"first_name" : "Matteo",
                "last_name" : "Cardelli",
                "age" : "19",
                "city" : "Rome"}
print(person["first_name"])
print(person["last_name"])
print(person["age"])
print(person["city"])
print("\n")

#6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers. Think of five names, and use them as keys in your dictionary. 
#Think of a favorite number for each person, and store each as a value in your dictionary. Print each person’s name and their favorite number. 
#For even more fun, poll a few friends and get some actual data for your program.
person: dict = {"Matteo" : "24",
                "Bruno" : "17",
                "Gabriela" : "07",
                "Lorenzo" : "33",
                "Alessandro" : "55"}
print(person)
print("\n")

#6-3. Glossary: A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
#• Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
#• Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and 
#then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.
glossary: dict = {"Matteo" : "24",
                "Bruno" : "17",
                "Gabriela" : "07",
                "Lorenzo" : "33",
                "Alessandro" : "55"}
print("Glossary\n")
print("Matteo :", glossary["Matteo"], "\n")
print("Bruno :", glossary["Bruno"], "\n")
print("Gabriela :", glossary["Gabriela"], "\n")
print("Lorenzo :", glossary["Lorenzo"], "\n")
print("Alessandro :", glossary["Alessandro"], "\n")


#6-7. People: Start with the program you wrote for Exercise 6-1. Make two new dictionaries representing different people, 
#and store all three dictionaries in a list called people. Loop through your list of people. As you loop through the list, 
#print everything you know about each person.
matteo: dict = {"first_name" : "Matteo",
                "last_name" : "Cardelli",
                "age" : "19",
                "city" : "Rome"}
lorenzo: dict = {"first_name" : "Lorenzo",
                "last_name" : "Brussani",
                "age" : "26",
                "city" : "Rome"}
gabriela: dict = {"first_name" : "Gabriela",
                "last_name" : "Ciuica",
                "age" : "21",
                "city" : "Rome"}

people: list = [matteo, lorenzo, gabriela]

for person in people:
    print(f"Name : {person['first_name']}")
    print(f"Surname : {person['last_name']}")
    print(f"Age : {person['age']}")
    print(f"City : {person['city']}")
    
    print()
    


#6-8. Pets: Make several dictionaries, where each dictionary represents a different pet. In each dictionary, 
#include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and as
#you do, print everything you know about each pet. 
dog: dict = {
    "owner" : "Matteo",
    "kind" : "Dog"
}
cat: dict = {
    "owner" : "Gabriela",
    "kind" : "Cat"
}
fish: dict = {
    "owner" : "Bruno",
    "kind" : "Fish"
}
rabbit: dict = {
    "owner" : "Giovanni",
    "kind" : "Rabbit"
}

pets: list = [dog, cat, fish, rabbit]

for pet_information in pets:
    print()
    print(f"Owner : {pet_information['owner']}")
    print(f"Kind : {pet_information['kind']}")
    
    print()


#6-9. Favorite Places: Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary, and store one to 
#three favorite places for each person. To make this exercise a bit more interesting, ask some friends to name a few of their favorite 
#places. Loop through the dictionary, and print each person’s name and their favorite places.
favourite_places: dict = {
    "Matteo" : ["Londra", "Parigi", "Barcellona"],
    "Bruno" : ["Alicante", "Rio", "Tokyo"],
    "Lorenzo" : ["LasVegas", "Miami", "LosAngeles"]                          
}

for person, places in favourite_places.items():
    print()
    print(f"Name : {person}")
    for place in places:
        print(f"favourtite places : {place}")


    print()


#6-10. Favorite Numbers: Modify your program from Exercise 6-2 so each person can have more than one favorite number. 
#Then print each person’s name along with their favorite numbers.
person: dict = {
    "Matteo" : ["24", "12", "96"],
    "Bruno" : ["17", "45", "69"],
    "Gabriela" : ["07", "74", "15"],
    "Lorenzo" : ["33", "63", "85"],
    "Alessandro" : ["55", "79", "23"]
}
for people, numbers in person.items():
    print()
    print(f"Name : {people}")
    for number in numbers:
        print(f"Favourite numbers : {number}")

print("\n")


#6-11. Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary. 
#Create a dictionary of information about each city and include the country that the city is in, its approximate population, 
#and one fact about that city. The keys for each city’s dictionary should be something like country, population, and fact. 
#Print the name of each city and all of the information you have stored about it.
Rome: dict = {
    "City" : "Rome",
    "Country" : "Italy", 
    "Population" : "2,873 milion"
}
Shanghai: dict = {
    "City" : "Shanghai", 
    "Country" : "Cina", 
    "Population" : "26,32 milion"
}
Paris: dict = {
    "City" : "Paris",
    "Country" : "France", 
    "Population" : "2,161 milion"
}

cities: dict = {"Rome" : Rome, "Shanghai" : Shanghai, "Paris" : Paris}
for city in cities:
    print(city)
    for k in cities[city]:
     message = f"{k}:  {cities[city][k]}"
     print(message)
    
print()


#6-12. Extensions: We’re now working with examples that are complex enough that they can be extended in any number of ways. 
#Use one of the example programs from this chapter, and extend it by adding new keys and values, changing the context of the program, 
#or improving the formatting of the output.
random_number = random.randint(0, 10)
number = int(input("inserisci un numero da 1 a 10 :"))

while number != random_number:
    print("You Lose")
    number = int(input("inserisci un numero da 1 a  :"))

print("You win")
    

    

    
    
    