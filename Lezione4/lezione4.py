#8-1. Message: Write a function called display_message() that prints one sentence telling everyone what you are learning about in this chapter. 
#Call the function, and make sure the message displays correctly.
def display_message() -> None:
    print("I'm studying the function")
display_message()

print("\n")



#8-2. Favorite Book: Write a function called favorite_book() that accepts one parameter, title. The function should print a message, 
#such as "One of my favorite books is Alice in Wonderland". Call the function, making sure to include a book title as an argument in the function call.
def favourite_book(book_name: str) -> None:
        print(f"One of my favorite books is {book_name}")
favourite_book(book_name= "'The Canterville Ghost'")

print("\n")



#8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. 
#The function should print a sentence summarizing the size of the shirt and the message printed on it. Call the function once using positional arguments to make a shirt. 
#Call the function a second time using keyword arguments.
def make_shirt(size: str, text: str) -> None:
      message: str = f"Size : {size}\nText : {text}"
      print(message)
make_shirt(size="M", text="-50%")
print()
make_shirt("M", "-50%")
print("\n")



#8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 
#Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.
def make_shirt(size: str = "L", text: str = "I love Python") -> None:
      message: str = f"Size : {size}\nText : {text}"
      print(message)
make_shirt()
print()
make_shirt(size="M", text="I love Python")
print()
make_shirt(size="XL", text="Is very big")

print("\n")



#8-5. Cities: Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence, 
#such as Reykjavik is in Iceland. Give the parameter for the country a default value. Call your function for three different cities, at least one 
#of which is not in the default country.
def describe_city(name: str, country: str = "USA") -> None:
      message: str = f"{name} is in {country}"
      print(message)
describe_city(name="Miami")
print()
describe_city(name="LasVegas")
print()
describe_city(name="Bangkok", country="Thilandia")
print("\n")



#8-6. City Names: Write a function called city_country() that takes in the name of a city and its country. The function should return a string 
#formatted like this: "Santiago, Chile". Call your function with at least three city-country pairs, and print the values that are returned.
def city_country(name: str, country: str) -> str:
      message: str = (f"{name}, {country} ")
      return(message)
rome_italy = city_country(name="Rome", country="Italy")
print(rome_italy)
print()
paris_france = city_country(name="Paris", country="France")
print(paris_france)
print()
barcelona_spain = city_country(name="Barcelona", country="Spain")
print(barcelona_spain)
print("\n")


#8-7. Album: Write a function called make_album() that builds a dictionary describing a music album. The function should take in an artist 
#name and an album title, and it should return a dictionary containing these two pieces of information. Use the function to make three dictionaries 
#representing different albums. Print each return value to show that the  dictionaries are storing the album information correctly. 
#Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. If the calling line includes a value 
#for the number of songs, add that value to the album’s dictionary. Make at least one new function call that includes the number of songs on an album.
#def make-album()
def make_album(name , titles, num_song = None) -> dict:
      album: dict ={ 
            "Artist".upper(): name,
            "Title".upper() : titles
      }
      if num_song:
            album['Num_songs'.upper()] = num_song
      return album
album1 = make_album("Gemitaiz", "Eclissi", 13)
album2 = make_album("Nayt", "Doom")
album3 = make_album("Mostro", "The Illest Vol.3")

print(album1)
print(album2)
print(album3)

print("\n")



#8-8. User Albums: Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist and title. 
#Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. Be sure to include a quit value in the while loop.
start = input("Do you want enter a new dictionary? Y/N ")
if start.upper() == "Y":
      x: bool= True
      album: list = []
      while x:
            name_artist = input("Enter the artist's name :")
            album_artist = input("Enter the album's name :")
            album.append(make_album(name_artist, album_artist))
            if input("Do you want to continue or quit ?") == "continue":
                  continue
            else:
                  break
      print(album)

print("\n")



#8-9. Messages: Make a list containing a series of short text messages. Pass the list to a function called show_messages(), which prints each text message.
messages: list = ["Good morning", "Helo", "How are you?"]
def show_messages(message: list) ->str:
      for sms in message:
           print(sms) 

show_messages(messages)

print("\n")



#8-10. Sending Messages: Start with a copy of your program from Exercise 8-9. Write a function called send_messages() that prints each text 
#message and moves each message to a new list called sent_messages as it’s printed. After calling the function, print both of your lists to make sure 
#the messages were moved correctly.
messages: list = ["Good morning", "Helo", "How are you?"]
def show_messages(message: list) ->str:
      sent_messages: list = []
      for sms in message:
           sent_messages.append(sms)
           print(sent_messages)

      return sent_messages

sent_messages = show_messages(messages)

print("\n")



#8-11. Archived Messages: Start with your work from Exercise 8-10. Call the function send_messages() with a copy of the list of messages. 
#After calling the function, print both of your lists to show that the original list has retained its messages.
messages: list = ["Good morning", "Helo", "How are you?"]
def show_messages(message: list) ->str:
      send_messages: list = []
      for sms in message:
           send_messages.append(sms)
      print(message.remove(sms))
      print(send_messages)
      return send_messages

send_messages = show_messages(messages)

print("\n")



#8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. The function should have one parameter 
#that collects as many items as the function call provides, and it should print a summary of the sandwich that’s being ordered. 
#Call the function three times, using a different number of arguments each time.
def sandwich(*args):
      print("Ingredients list :")
      for ing in args:
            print(f"\t-{ing}")

sandwich("Bread", "tomatoes", "salad", "ham", "cheese")
      
print("\n")



#8-13. User Profile:  Build a profile of yourself by calling build_profile(), using your first and last names and three other key-value pairs 
#that describe you. All the values must be passed to the function as parameters. The function then must return a string such as "Eric Crow, age 45, hair brown, weight 67"
def build_profile(name: str = "Leonardo", lastname: str = "Brussani", age: int = 20, high: float = 1.80) -> str:
      return(f"{name} {lastname}, age {age} anni, {high}m")

my_profile = build_profile()
print(my_profile)

print("\n")



#8-14. Cars: Write a function that stores information about a car in a dictionary. The function should always receive a manufacturer and a model name. 
#It should then accept an arbitrary number of keyword arguments. Call the function with the required information and two other name-value pairs, 
#such as a color or an optional feature. Your function should work for a call like this one: car = make_car('subaru', 'outback', color='blue', tow_package=True) 
#Print the dictionary that’s returned to make sure all the information was stored correctly. 
def make_car(model, color, weigth) -> dict:
      car_id: dict = {
            "Model".upper() : model,
            "Color".upper() : color,
            "Wight".upper() : weigth
      }
      return car_id
car = make_car("Porsche", "Grey", "1.430 kg")
print(car)

print("\n")



#8-15. Printing Models: Put the functions for the example printing_models.py in a separate file called printing_functions.py. 
#Write an import statement at the top of printing_models.py, and modify the file to use the imported functions.
#import pandas
#dataframe = pandas.read_csv("filename")
#print("\n")



#8-16. Imports: Using a program you wrote that has one function in it, store that function in a separate file. Import the function into your main program file, 
#and call the function using each of these approaches:
#import pandas
#from  pandas import read_csv
#from pandas import DataFrame as df
#import pandas as pd
#from pandas import *
#print("\n")



#8-17. Styling Functions: Choose any three programs you wrote for this chapter, and make sure they follow the styling guidelines described in this section.

#Done

#Questa funzione serve per implementare Bubble sort
import time

def bubble_sort(a: list) -> list:
      for i in range(len(a)):
            swap_flag = False
            for j in range(len(a)-i-1):
                  if (a[j] > a[j+1]):
                        swap_flag = True
                        temp: int = a[j]
                        a[j] = a[j+1]
                        a[j+1] = temp
            if swap_flag is False:
                  return a    
      
a: list = [2, 3, 30, 26, 45, 75]
start: int = time.time()
bubble_sort(a)
print(time.time()- start)
print(a)
