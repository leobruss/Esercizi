class Media:
    def __init__(self) -> None:
        #Il titolo del media.
        self.title: str = None
        #Una lista di valutazioni del media, con voti compresi tra 1 e 5.
        self.reviews: list[int] = []

    #Imposta il titolo del media.
    def set_title(self, title: str) ->None:
        self.title = title

    #Restituisce il titolo del media.
    def get_title(self) ->str:
        return self.title
    
    #Aggiunge una valutazione alla lista delle recensioni se è valida (tra 1 e 5).
    def aggiungiValutazione(self, voto: int) -> None:
        if 1 <= voto <= 5:
            self.reviews.append(voto)

    #Calcola e restituisce la media delle valutazioni.
    def getMedia(self) ->float:
        media = sum(self.reviews) / len(self.reviews)
        return media
        
    #Restituisce una stringa che descrive il giudizio medio del media basato sulla media delle valutazioni.
    def getRate(self) ->str:
        if self.getMedia() <= 1:
            print("Terribile")
        elif self.getMedia() <= 2:
            print("Brutto")
        elif self.getMedia() <= 3:
            print("Normale")
        elif self.getMedia() <= 4:
            print("Bello")
        elif self.getMedia() <= 5:
            print("Stupendo")

    #Calcola e restituisce la percentuale di un voto specifico nelle recensioni.
    def ratePercentage(self, voto: int) ->str:
       return(self.reviews.count(voto) / len(self.reviews)) * 100
    
    #Mostra un riassunto delle recensioni e delle valutazioni del media, stampando il titolo, il voto medio, il giudizio e le percentuali di ciascun voto
    def recensione(self) ->str:
        print(f"Titolo del Film: {self.get_title()}\nVoto Medio: {self.getMedia()}\nGiudizio: {self.getRate()}\nTerribile: {self.ratePercentage(0)}\nBrutto: {self.ratePercentage(1)}\nNormale: {self.ratePercentage(2)}\nBello: {self.ratePercentage(3)}\nGrandioso: {self.ratePercentage(4)}")

            
film_title = Media()

film_title.set_title("Shining")
film_title.aggiungiValutazione(1)
film_title.aggiungiValutazione(3)
film_title.aggiungiValutazione(2)
film_title.aggiungiValutazione(1)
film_title.aggiungiValutazione(5)
film_title.aggiungiValutazione(4)
film_title.aggiungiValutazione(4)
film_title.aggiungiValutazione(5)
film_title.aggiungiValutazione(3)
film_title.aggiungiValutazione(4)

print(film_title.ratePercentage(1))
print(film_title.ratePercentage(2))
print(film_title.ratePercentage(3))
print(film_title.ratePercentage(4))
print(film_title.ratePercentage(5))

film_title.recensione()