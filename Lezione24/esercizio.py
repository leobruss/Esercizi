class Documento():
    def __init__(self) -> None:
        self.testo = None

    # Getters ----------------------------------------------------------------
    @property
    def getText(self) -> str:
        return self.testo

    # Setters ----------------------------------------------------------------
    @getText.setter
    def setText(self, text: str) -> None:
        self.testo: str = text

    # Others -----------------------------------------------------------------
    def isInText(self, keyword: str) -> bool:
        if self.testo:
            if keyword in self.testo:
                return True
            else:
                return False
      

            
class Email(Documento):
    def __init__(self) -> None:
        super().__init__()
        self._mittente: str = None
        self._destinatario: str = None
        self._titolo: str = None

    # Getters ----------------------------------------------------------------
    @property
    def getMittente(self) -> str:
        return self._mittente
    
    @property
    def getDestinatario(self) -> str:
        return self._destinatario
    
    @property
    def getTitolo(self) -> str:
        return self._titolo
    
    # Setters ----------------------------------------------------------------
    @getMittente.setter
    def setMittente(self, value: str) -> None:
        self._mittente = value

    @getDestinatario.setter
    def setDestinatario(self, value: str) -> None:
        self._destinatario = value

    @getTitolo.setter
    def setTitolo(self, value: str) -> None:
        self._titolo = value

    # Others -----------------------------------------------------------------
