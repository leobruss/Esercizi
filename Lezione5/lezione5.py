#1. Create a Playlist:

#Write a function called create_playlist() that accepts a playlist name and a variable number of song titles. The function should return a dictionary with 
#the playlist name and a set of songs. Call the function with different numbers of songs to demonstrate flexibility.

#Example: create_playlist("Road Trip", {"Song 1", "Song 2"})
#Write a function called add_like() that accepts a dictionary, the name of a playlist, and a boolean value indicating whether it is liked (True or False). 
#This function should return an updated dictionary
#Example: add_like(dictionary, “Road Trip”, liked=True)
def create_playlist(playlist_name, *songs) ->dict:
    playlist = {
        "name": playlist_name,
        "songs": set(songs)
    }
    return playlist

def add_like(playlists_dict, playlist_name, liked=True):
    for playlist in playlists_dict:
        if playlist["name"] == playlist_name:
            playlist["liked"] = liked
            break
    return playlists_dict



#
playlist1 = create_playlist("QVC10", "Ballon d'or", "Jeffrey", "La ballata del dubbio pt4")
playlist2 = create_playlist("Habitat", "Se ne va", "No more drama")
playlist3 = create_playlist("Eclissi", "Silenzio", "Qua cont te", "Adesso")

playlists = [playlist1, playlist2, playlist3]


playlists = add_like(playlists, "QVC10  ", liked=False)


for playlist in playlists:
    print("Playlist:", playlist["name"])
    print("Songs:", playlist["songs"])
    print("Liked:", playlist.get("liked", False))
    print()





#2. Book Collection:
#Write a function called add_book() that accepts an author's name and a variable number of book titles authored by them. This function should return a dictionary 
#where the author's name is the key and the value is a list of their books. Demonstrate this function by adding books for different authors.
#Example: add_book("Mark Twain", ["The Adventures of Tom Sawyer", "Life on the Mississippi"])
#Write a function called delete_book() that accepts a dictionary and the name of the author from whom to remove all details. 
#This function should return an updated dictionary.
#Example: delete_book(dictionary, “Mark Twain”)
def add_book(author_name, *book_titles) ->dict:
    
    if 'library' not in globals():
        global library
        library = {}
    
    if author_name in library:
        library[author_name].extend(book_titles)
    else:
        library[author_name] = list(book_titles)
    
    return library

def delete_book(library, author_name):
    
    if author_name in library:
        del library[author_name]
    
    return library


add_book("Mark Twain", "The Adventures of Tom Sawyer", "Life on the Mississippi")
add_book("J.K. Rowling", "Harry Potter and the Philosopher's Stone", "Harry Potter and the Chamber of Secrets")
add_book("George Orwell", "1984", "Animal Farm")

print("Library after adding books:")
print(library)

delete_book(library, "Mark Twain")
print("\nLibrary after deleting Mark Twain's books:")
print(library)

print("\n")



#3. Personal Info:

#Write a build_profile() function that accepts the name , surname,  occupation, location, and age  of a person. Make occupation, location, 
#and age optional parameters. Use this function to create profiles for different people, demonstrating how it handles these optional parameters.
#Example: build_profile("John", "Doe", occupation="Developer", location="USA", age=30)
def build_profile(name, surname, occupation=None, location=None, age=None):
    profile = {
        "name": name,
        "surname": surname
    }
    
    if occupation is not None:
        profile["occupation"] = occupation
    if location is not None:
        profile["location"] = location
    if age is not None:
        profile["age"] = age
    
    return profile

profile1 = build_profile("Leonardo", "Brussani", occupation="Cyber Security specialist", location="Italy", age=19)
print("Profile 1:", profile1)

profile2 = build_profile("Lorenzo", "Brussani", occupation="financial advisor", age=26)
print("Profile 2:", profile2)

profile3 = build_profile("Gianluca", "Brussani", location="Italy")
print("Profile 3:", profile3)





#4. Event Organizer:

#Write a function called plan_event() that accepts an event name, a list of participants, and an hour. The function should return a dictionary 
#that includes the event name and a list of the participants. Call this function with varying numbers of participants to plan different events.

#Example: plan_event("Code Workshop", ["Alice", "Bob", "Charlie"],”4pm”)

#Write a function called modify_event() that accepts a dictionary, an event name, and new details to modify an already planned event.

#Example: modify_event(dictionary, "Code Workshop", ["Alice", "Bob", "Charlie"], ”4pm”)

def plan_event(event_name: str, list_of_participants: list, hour: float) ->dict:
    event: dict ={
        "Name" : event_name,
        "List of participants" : list_of_participants
    }
    return event
def modify_event(dictionary: dict, event_name: str, list_of_participants: list, hour: float):
    for dict in dictionary:
        



#5. Shopping List:

#Write a function called create_shopping_list() that accepts a store name and any number of items as arguments. It should return a dictionary with the store name and a set of items to buy there. Test the function with different stores and item lists.

#Example: create_shopping_list("Grocery Store", {"Milk", "Eggs", "Bread"})

#Write a function called print_shopping_list() that accepts a dictionary and a store name, then prints each item from that store's shopping list.

#Example: print_shopping_list(dictionary, "Grocery Store")