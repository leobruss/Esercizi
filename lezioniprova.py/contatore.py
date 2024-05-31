class Contatore:
    def __init__(self) -> None:
        self.conteggio = 0

    def setZero(self) -> None:
        self.conteggio = 0
    
    def add1(self) -> None:
        self.conteggio += 1

    def sub1(self) -> None:
        if self.conteggio >= 1:
            self.conteggio -= 1
        else:
            print(f"Non è possibile eseguire la sottrazione ")

    def get(self) -> None:
        return self.conteggio

    def mostra(self) -> None:
        print(f"Conteggio attuale: {self.conteggio}")

c = Contatore()
c.add1()
c.mostra()

	
c = Contatore()
c.add1()
c.add1()
c.add1()
c.mostra()

	
c = Contatore()
c.sub1()
c.mostra()

	
c = Contatore()
c.add1()
c.add1()
c.add1()
c.add1()
c.sub1()
c.add1()
c.add1()
c.sub1()
c.mostra()

	
c = Contatore()
c.add1()
c.add1()
c.add1()
c.add1()
c.sub1()
c.add1()
c.add1()
z  = c.get()
print(z)


    
    
    