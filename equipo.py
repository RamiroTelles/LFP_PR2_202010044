class equipo():

    def __init__(self,nombre) -> None:
        self.nombre = nombre
        self.pj = 0
        self.g = 0
        self.e = 0
        self.p = 0
        self.gf = 0
        self.gc = 0
        self.dg = 0
        self.pts = 0
        pass

    def meterPartido(self,gf,gc):
        self.pj+=1
        if gf>gc:
            self.g+=1
        elif gc>gf:
            self.p+=1
        else:
            self.e+=1
        self.gf+=gf
        self.gc+=gc
        self.dg= self.gf -self.gc
        self.pts = 3* (self.g) + self.e

