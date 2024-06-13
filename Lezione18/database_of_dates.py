#Database of dates:  
#Write a class that manages a database of dates with the format gg.mm.aaaa implementing methods to add a new date, 
#delete a given date, modify a date, and perform a query on a given date is required.  
#A query on a given date allows for retrieving a given new date. Note that a date is an object for your database; 
#it must be instantiated from a string.

class Database:
    def __init__(self) -> None:
        self.dates: list = []

    def add_data(self, dates: str) ->None:
        if dates not in self.dates:
            self.dates.append(dates)

    def remove_data(self, dates: str) ->None:
        if dates in self.dates:
            self.dates.remove(dates)
    
    def modify_data(self, dates: str, new_date: str) ->None:
        if dates in self.dates:
            for i in range(len( self.dates)):
                if  self.dates[i] == dates:
                 self.dates[i] = new_date

            

    def given_date(self):
        return self.dates
    

date: Database = Database()

date.add_data("24/07/2004")
date.add_data("09/11/1997")
date.add_data("10/06/1968")
date.add_data("21/07/1960")

date.remove_data("09/11/1997")

date.modify_data("10/06/1968", "10/06/1969")

print(date.given_date())
