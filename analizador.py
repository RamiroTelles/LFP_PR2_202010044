from contextlib import nullcontext
from enum import Flag
from fileinput import filename
from Eltoken import token
from tokentype import tokentype

class analizador():
    
    def __init__(self) -> None:
        self.errorLexico=""
        self.errorSintactico=""
        self.tokens=[]
        self.tokensActuales=[]
        pass

    def restartLogs(self):
        self.errorLexico = ""
        self.errorSintactico =""
        self.tokens= []
        self.tokensActuales=[]

    def analLexico(self,txt):
        estado=0
        lexema=""
        columna=1
        fila=1
        errores=""
        
        i=0
        actual=""
        long = len(txt)
        while(i<long and txt[i]!=None):

            actual=txt[i]
            if estado==0 :
                if actual.isalpha():
                    lexema+=actual
                    estado=1
                    i+=1
                    columna+=1
                    continue
                elif actual == "\"":
                    estado=2
                    lexema+=actual
                    i+=1
                    columna+=1
                    continue
                elif actual== "-":
                    estado = 4
                    lexema+=actual
                    i+=1
                    columna+=1
                    continue
                elif actual.isdigit():
                    estado =6
                    lexema+=actual
                    i+=1
                    columna+=1
                    continue
                elif actual== "<":
                    estado=7
                    lexema+=actual
                    i+=1
                    columna+=1
                    continue
                elif actual== " ":
                    i+=1
                    columna+=1
                    continue
                elif actual == "\t":
                    i+=1
                    columna+=5
                    continue
                elif actual == "\n":
                    i+=1
                    columna=1
                    fila+=1
                    continue
                elif actual == "\r":
                    i+=1
                    columna+=1
                    continue
                else: 
                    #print("Simbolo " + actual + " no reconocido")
                    errores+= "Simbolo "+ actual + " no reconocido en columna: "+ str(columna) + " fila: "+ str(fila)+ "\n"
                    i+=1
                    columna+=1
                    continue

            elif estado==1:
                if actual != " " or actual!= "\t" or actual!= "\n" or actual!= "\r":
                    lexema+=actual
                    i+=1
                    columna+=1
                    continue
                else:
                    self.tokens.append(token(tokentype.letras,lexema,fila,columna))
                    self.tokensActuales.append(token(tokentype.letras,lexema,fila,columna))
                    lexema=""
                    estado=0
                    continue
            elif estado==2:
                if actual=="\"":
                    estado=0
                    lexema+=actual
                    self.tokens.append(token(tokentype.cadena,lexema,fila,columna))
                    self.tokensActuales.append(token(tokentype.cadena,lexema,fila,columna))
                    lexema=""
                    i+=1
                    columna+=1
                    continue
                elif actual=="\n":
                    lexema+=actual
                    i+=1
                    columna=1
                    fila+=1
                    continue
                elif actual =="\t":
                    lexema+=actual
                    i+=1
                    columna+=5
                    continue
                else:
                    lexema+=actual
                    i+=1
                    columna+=1
                    continue
            elif estado==4:
                if actual.isalpha():
                    estado=5
                    lexema+=actual
                    columna+=1
                    i+=1
                    continue
                else:
                    errores+="Se esperaba una letra en la columna "+ str(columna) + ". fila "+ str(fila)+ "\n"
            elif estado==5:
                if actual.isalpha():
                    
                    lexema+=actual
                    columna+=1
                    i+=1
                    continue
                else:
                    estado=0
                    self.tokens.append(token(tokentype.flag,lexema,fila,columna))
                    self.tokensActuales.append(token(tokentype.flag,lexema,fila,columna))
                    lexema=""
                    continue
            elif estado ==6:
                if actual.isdigit():
                    lexema+=actual
                    estado=0
                    self.tokens.append(token(tokentype.num,lexema,fila,columna))
                    self.tokensActuales.append(token(tokentype.num,lexema,fila,columna))
                    lexema=""
                    i+=1
                    columna+=1
                    continue
                else:
                    self.tokens.append(token(tokentype.num,lexema,fila,columna))
                    self.tokensActuales.append(token(tokentype.num,lexema,fila,columna))
                    lexema=""
                    estado=0
                    continue
            elif estado==7:
                if actual.isdigit():
                    estado=8
                    lexema+=actual
                    i+=1
                    columna+=1
                    continue
                else:
                    errores+="Se esperaba un digito en la columna "+ str(columna) + ". fila "+ str(fila)+ "\n"
            elif estado==8:
                if actual.isdigit():
                    estado=9
                    lexema+=actual
                    i+=1
                    columna+=1
                    continue
                else:
                    errores+="Se esperaba un digito en la columna "+ str(columna) + ". fila "+ str(fila)+ "\n"
            elif estado==9:
                if actual.isdigit():
                    estado=10
                    lexema+=actual
                    i+=1
                    columna+=1
                    continue
                else:
                    errores+="Se esperaba un digito en la columna "+ str(columna) + ". fila "+ str(fila)+ "\n"
            elif estado==10:
                if actual.isdigit():
                    estado=11
                    lexema+=actual
                    i+=1
                    columna+=1
                    continue
                else:
                    errores+="Se esperaba un digito en la columna "+ str(columna) + ". fila "+ str(fila)+ "\n"
            elif estado==11:
                if actual =="-":
                    estado=12
                    lexema+=actual
                    i+=1
                    columna+=1
                    continue
                else:
                    errores+="Se esperaba un - en la columna "+ str(columna) + ". fila "+ str(fila)+ "\n"
            elif estado==12:
                if actual.isdigit():
                    estado=13
                    lexema+=actual
                    i+=1
                    columna+=1
                    continue
                else:
                    errores+="Se esperaba un digito en la columna "+ str(columna) + ". fila "+ str(fila)+ "\n"
            elif estado==13:
                if actual.isdigit():
                    estado=14
                    lexema+=actual
                    i+=1
                    columna+=1
                    continue
                else:
                    errores+="Se esperaba un digito en la columna "+ str(columna) + ". fila "+ str(fila)+ "\n"
            elif estado==14:
                if actual.isdigit():
                    estado=15
                    lexema+=actual
                    i+=1
                    columna+=1
                    continue
                else:
                    errores+="Se esperaba un digito en la columna "+ str(columna) + ". fila "+ str(fila)+ "\n"
            elif estado==15:
                if actual.isdigit():
                    estado=16
                    lexema+=actual
                    i+=1
                    columna+=1
                    continue
                else:
                    errores+="Se esperaba un digito en la columna "+ str(columna) + ". fila "+ str(fila)+ "\n"
            elif estado==16:
                if actual == ">":
                    
                    lexema+=actual
                    estado=0
                    self.tokens.append(token(tokentype.year,lexema,fila,columna))
                    self.tokensActuales.append(token(tokentype.year,lexema,fila,columna))
                    i+=1
                    columna+=1
                    continue
                else:
                    errores+="Se esperaba un > en la columna "+ str(columna) + ". fila "+ str(fila)+ "\n"
        self.errorLexico = errores
        pass

    #def analSintactico(self):
      #  pila=[]
      #  self.tokensActuales.append("#")
      #  pila.append("#")
      #  #pila.append("S")
      #  #pila.pop()
      #  pila.append("S1")
      #  pila.append(tokentype.letras)
      #  for obj in self.tokensActuales:
     #       actual = pila.pop()
     #       if actual == obj.type:
     #           continue
     #       if actual == "S1":
     #           if self.tokensActuales[0].lexema == "RESULTADO":
     #               pass


    #    pass

    def analSintactico(self):
        self.tokensActuales.append(token(tokentype.tokenAceptacion,"#",0,0))
        self.pos=0
        self.tokenAc = self.tokensActuales[self.pos]
        self.inicio()

    def comparar(self,tipo):
        error = True
        if self.tokenAc.type != tipo:
            self.errorSintactico+= "Se esperaba un " + tipo + " en la columna " + str(self.tokenAc.columna) + ". fila " + str(self.tokenAc.fila) + "\n"
            error= False

        #if self.tokenAc.type != tipo:
         #   self.pos+=1
          #  self.tokenAc = self.tokensActuales[self.pos]

        if self.tokenAc.type == tokentype.tokenAceptacion:
            print("analisis sintactico finalizado")
        return error
    
    def compararPR(self,tipo,lexema):
        error = True
        if self.tokenAc.type != tipo:
            self.errorSintactico+= "Se esperaba un " + tipo + " en la columna " + str(self.tokenAc.columna) + ". fila " + str(self.tokenAc.fila) + "\n"
            error = False

        #if self.tokenAc.type != tokentype.tokenAceptacion and lexema == self.tokenAc.lexema:
           # self.pos+=1
            #self.tokenAc = self.tokensActuales[self.pos]
        if lexema != self.tokenAc.lexema:
            self.errorSintactico+="Se esperaba la palabra reservada " + lexema + " en la columna " + str(self.tokenAc.columna) + ". fila " + str(self.tokenAc.fila) + "\n"
            error=False

        if self.tokenAc.type == tokentype.tokenAceptacion:
            print("analisis sintactico finalizado")
        return error

    def inicio(self):
        if self.tokenAc.lexema == "RESULTADO":
            self.resultados()
            print("funcion RESULTADO")
            pass
        if self.tokenAc.lexema == "JORNADA":
            self.jornada()
            print("funcion JORNADA")
            pass
        if self.tokenAc.lexema == "GOLES":
            self.goles()
            print("funcion goles")
            pass
        if self.tokenAc.lexema == "TABLA":
            #self.tabla()
            print("funcion tabla")
            pass
        if self.tokenAc.lexema == "PARTIDOS":
            #self.partidos()
            print("funcion Partidos")
            pass
        if self.tokenAc.lexema == "TOP":
            #self.top()
            print("funcion Top")
            pass
        if self.tokenAc.lexema == "ADIOS":
            #self.adios()
            print("funcion ADIOS")
            pass

    def resultados(self):
        self.compararPR(tokentype.letras,"RESULTADO")
        self.avanzar()
        
        if self.comparar(tokentype.cadena):
            equipo1 = self.tokenAc.lexema
        self.avanzar()    

        self.compararPR(tokentype.letras,"VS")
        self.avanzar()

        if self.comparar(tokentype.cadena):
            equipo2 = self.tokenAc.lexema
        self.avanzar()

        self.compararPR(tokentype.letras,"TEMPORADA")
        self.avanzar()

        if self.comparar(tokentype.year):
            rangoTemporada = self.tokenAc.lexema
        self.avanzar()

        if equipo1!=None or equipo2 != None or rangoTemporada!= None:
            print("realizar resultados con " + equipo1 + ", " + equipo2+ ",temporada " + rangoTemporada)

    def jornada(self):
        self.compararPR(tokentype.letras,"JORNADA")
        self.avanzar()
        
        if self.comparar(tokentype.num):
            jornada = self.tokenAc.lexema
        self.avanzar()    

        self.compararPR(tokentype.letras,"TEMPORADA")
        self.avanzar()

        if self.comparar(tokentype.year):
            rangoTemporada = self.tokenAc.lexema
        self.avanzar()

        banderas = self.S3("jornada")


        if jornada!=None or rangoTemporada!= None:
            print("realizar jornada con numero " + jornada + ",temporada " + rangoTemporada +" y nombre de archivo " + banderas[0])


    def goles(self):

        self.compararPR(tokentype.letras,"GOLES")
        self.avanzar()

        if self.compararPR(tokentype.letras,"LOCAL") or self.compararPR(tokentype.letras,"VISITANTE") or self.compararPR(tokentype.letras,"TOTAL"):
            condicion = self.tokenAc.lexema
        self.avanzar()

        if self.comparar(tokentype.cadena):
            equipo = self.tokenAc.lexema
        self.avanzar()

        self.compararPR(tokentype.letras,"TEMPORADA")
        self.avanzar()

        if self.comparar(tokentype.year):
            rangoTemporada = self.tokenAc.lexema
        self.avanzar()

        if condicion!=None or equipo != None or rangoTemporada!= None: 
            print("realizar goles con " + condicion + ",equipo " + equipo +" y rango temporada " + rangoTemporada)

    def tabla(self):
        self.compararPR(tokentype.letras,"TABLA")
        self.avanzar()

        self.compararPR(tokentype.letras,"TEMPORADA")
        self.avanzar()

        if self.comparar(tokentype.year):
            rangoTemporada = self.tokenAc.lexema
        self.avanzar()

        banderas = self.S3()

        if rangoTemporada!= None: 
            print("realizar tabla con rango temporada " + rangoTemporada + "y nombre de archivo " + banderas[0])

    def partidos(self):
        self.compararPR(tokentype.letras,"PARTIDOS")
        self.avanzar()

        if self.comparar(tokentype.cadena):
            equipo = self.tokenAc.lexema
        self.avanzar()

        self.compararPR(tokentype.letras,"TEMPORADA")
        self.avanzar()

        if self.comparar(tokentype.year):
            rangoTemporada = self.tokenAc.lexema
        self.avanzar()

        banderas = self.S3()

        if equipo != None or rangoTemporada!= None: 
            print("realizar partidos con equipo " + equipo +" y rango temporada " + rangoTemporada + " con nombre de archivo " + banderas[0] + " , con jornada inicial " + banderas[2] + ", y con jornada final " + banderas[3])

    def top(self):
        self.compararPR(tokentype.letras,"TOP")
        self.avanzar()

        if self.compararPR(tokentype.letras,"SUPERIOR") or self.compararPR(tokentype.letras,"INFERIOR"):
            condicion = self.tokenAc.lexema
        self.avanzar()

        self.compararPR(tokentype.letras,"TEMPORADA")
        self.avanzar()

        if self.comparar(tokentype.year):
            rangoTemporada = self.tokenAc.lexema
        self.avanzar()

        banderas = self.S3()

        if condicion!=None or rangoTemporada!= None: 
            print("realizar goles con " + condicion + " y rango temporada " + rangoTemporada + ", con numero de " + banderas[1])

    def adios(self):
        if self.compararPR(tokentype.letras,"ADIOS"):
            self.avanzar()
            print("Salir de la aplicacion")





    def S3(self,titulo):
        n=5
        ji = 1 #jornada inicial defalut
        jf = 33 #jornada final default
        a = titulo
        if self.tokenAc.lexema == "-f":
            self.comparar(tokentype.flag)
            self.avanzar()
            if self.comparar(tokentype.letras):
                a = self.tokenAc.lexema
            else:
                self.errorSintactico += "Se esperaba un token letras en la columna " +str(self.tokenAc.columna)+ " y fila " +str(self.tokenAc.fila) + "\n"
            self.avanzar()
            self.S3(titulo)
        elif self.tokenAc.lexema == "-ji":
            self.comparar(tokentype.flag)
            self.avanzar()
            if self.comparar(tokentype.num):
                ji = int(self.tokenAc.lexema)
            else:
                self.errorSintactico += "Se esperaba un token numero en la columna " +str(self.tokenAc.columna)+ " y fila " +str(self.tokenAc.fila) + "\n"
            self.avanzar()
            self.S3(titulo)
        elif self.tokenAc.lexema == "-jf":
            self.comparar(tokentype.flag)
            self.avanzar()
            if self.comparar(tokentype.num):
                jf = int(self.tokenAc.lexema)
            else:
                self.errorSintactico += "Se esperaba un token numero en la columna " +str(self.tokenAc.columna)+ " y fila " +str(self.tokenAc.fila) + "\n"
            self.avanzar()
            self.S3(titulo)
        elif self.tokenAc.lexema == "-n":
            self.comparar(tokentype.flag)
            self.avanzar()
            if self.comparar(tokentype.num):
                n = int(self.tokenAc.lexema)
            else:
                self.errorSintactico += "Se esperaba un token numero en la columna " +str(self.tokenAc.columna)+ " y fila " +str(self.tokenAc.fila) + "\n"
            self.avanzar()
            self.S3(titulo)
        else:
            self.errorSintactico += "Se esperaba una palabra reservada en la columna " +str(self.tokenAc.columna)+ " y fila " +str(self.tokenAc.fila) + "\n"
        
        resul = []
        resul.append(a)
        resul.append(n)
        resul.append(ji)
        resul.append(jf)
        return resul




    def avanzar(self):
        self.pos+=1
        self.tokenAc = self.tokensActuales[self.pos]


