from asyncio.windows_events import ERROR_CONNECTION_ABORTED
from equipo import equipo
from partido import partido

class csv():

    def __init__(self) -> None:
        self.partidos=[]
        pass

    def leerCSV(self):
        try:
            path = "LaLigaBot-LFP.csv"
            

            with open(path,encoding='utf-8') as file:
                txt = file.read().strip()
                file.close()
        except:
            print("Error")

        txt = str(txt)

        filas = txt.split("\n")
        columnas=[]
        #partidos = []

        j=0
        for row in filas:
            if j==0:
                j+=1
                continue
            columnas = row.split(",")

            self.partidos.append(partido(columnas[1],columnas[2],columnas[3],columnas[4],columnas[5],columnas[6]))
        pass

    def resultados(self,equipo1,equipo2,temporada):
        temporada = temporada[1:-1]
        equipo1 = equipo1[1:-1]
        equipo2 = equipo2[1:-1]
        encontrado = False
        for obj in self.partidos:
            if obj.temporada == temporada and obj.equipo1 == equipo1 and obj.equipo2 == equipo2:
                partido1 = obj
                encontrado= True
        if encontrado:
            print("El resultado de este partido fue : " + partido1.equipo1 + " " + partido1.goles1 + " - " + partido1.equipo2 + " " + partido1.goles2)
        else:
            print("No encontrado")

    def jornada(self,jornada,temporada,nombreArchivo):
        temporada = temporada[1:-1]
        encontrado=False
        matches = []
        for obj in self.partidos:
            if obj.temporada == temporada and obj.jornada == jornada:
                matches.append(obj)
                encontrado=True

        if encontrado:
            print("Imprimir reporte de las jornadas")
        else:
            print("No encontrado")

    def goles(self,condicion,equipo,temporada):
        temporada = temporada[1:-1]
        equipo = equipo[1:-1]
        goles=0
        encontrado=False
        if condicion=="LOCAL" or condicion == "TOTAL":
            for obj in self.partidos:
                if obj.temporada == temporada and obj.equipo1 == equipo:
                    goles+= int(obj.goles1)
                    encontrado=True
        
        if condicion=="VISITANTE" or condicion == "TOTAL":
            for obj in self.partidos:
                if obj.temporada == temporada and obj.equipo2 == equipo:
                    goles+= int(obj.goles2)
                    encontrado=True

        if encontrado:
            print("Los goles anotados por el "+ equipo +" en total en la temporada "+ temporada +" fueron " + str(goles))
        else:
            print("No encontrado")

    def tabla(self,temporada):
        equipos = self.resumenTemporada(temporada)
        if equipos!=None:
            print("Crear el html de la liga")
        else:
            print("No encontrado")
        pass

    def resumenTemporada(self,temporada):
        equipos = []
        temporada = temporada[1:-1]
        encontrado=False
        partidosTemporada = []
        for obj in self.partidos:
            if obj.temporada == temporada:
                partidosTemporada.append(obj)
                if obj.jornada==1:
                    equipos.append(equipo(obj.equipo1))
                    equipos.append(equipo(obj.equipo2))
        
        for obj in partidosTemporada:
            for j in equipos:
                if obj.equipo1 == j.nombre:
                    j.meterPartido(obj.goles1,obj.goles2)
                if obj.equipo2 == j.nombre:
                    j.meterPartido(obj.goles2,obj.goles1)
        
        equipos = self.ordenarEquipos(equipos)

        return equipos
        
           
    def ordenarEquipos(self,equipos):
        
        for i in range(equipos.len):
            for j in range(equipos.len-1):
                if equipos[j].pts == equipos[j+1].pts:
                    if equipos[j].dg < equipos[j+1].dg:
                        aux = equipos[j]
                        equipos[j] = equipos[j+1]
                        equipos[j+1] = aux
                elif equipos[j].pts < equipos[j+1].pts:
                        aux = equipos[j]
                        equipos[j] = equipos[j+1]
                        equipos[j+1] = aux
        
        return equipos



    def partidos(self,equipo,temporada,a,ji,jf):
        temporada = temporada[1:-1]
        equipo = equipo[1:-1]
        matches = []
        encontrado=False
        for obj in self.partidos:
            if obj.temporada == temporada and (obj.equipo1 == equipo or obj.equipo2 == equipo) and obj.jorndada >= ji and obj.jornada <= jf:
                matches.append(obj)
                encontrado= True

        if encontrado:
            print("Imprimir el html con el nombre de a")
        else:
            print("No encontrado")

    def top(self,condicion,temporada,n):
        
        equipos = self.resumenTemporada(temporada)
        
        encontrado = False
        topEquipos = []
        if condicion=="SUPERIOR":
            for i in range(n):
                topEquipos.append(equipos[i])
        elif condicion=="INFERIOR":
            for i in range( (equipos.len-n), equipos.len):
                topEquipos.append(equipos[i])



    
