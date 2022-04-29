from csv import csv
from partido import partido

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
partidos = []

j=0
for row in filas:
    if j==0:
        j+=1
        continue
    columnas = row.split(",")

    partidos.append(partido(columnas[1],columnas[2],columnas[3],columnas[4],columnas[5],columnas[6]))

for i in range(5):
    print(partidos[i].temporada)
    print(partidos[i].jornada)
    print(partidos[i].equipo1)
    print(partidos[i].equipo2)
    print(partidos[i].goles1)
    print(partidos[i].goles2)


