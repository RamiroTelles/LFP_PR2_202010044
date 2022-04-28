from secrets import token_urlsafe


class analizador():
    
    def __init__(self) -> None:
        self.errorLexico=""
        self.errorSintactico=""
        self.tokens=[]
        pass

    def restartLogs(self):
        self.errorLexico = ""
        self.errorSintactico =""
        self.tokens= []

    def analLexico(self,txt):
        pass

    def analSintactico(self):
        pass
