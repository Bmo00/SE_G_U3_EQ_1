from statistics import stdev
import numpy as np
import pandas as pd

LPromedios=[];LDesvEsta=[]
Datos = pd.read_csv("../Archivos/Pokemones.csv", sep=',')

Ataque,Defensa,AtaqueEsp,DefensaEsp,Velocidad = Datos["Ataque"],Datos["Defensa"],Datos["AtqEsp"],Datos["DefEsp"],Datos["Velocidad"]

Ataque = Ataque.to_list()
Defensa = Defensa.to_list()
AtaqueEsp = AtaqueEsp.to_list()
DefensaEsp = DefensaEsp.to_list()
Velocidad = Velocidad.to_list()

Dic={"Atq":Ataque,"Def":Defensa,"AtqEsp":AtaqueEsp,"DefEsp":DefensaEsp,"Velocidad":Velocidad}

def estandarizacion(Diccionario):
    for i in Diccionario:
        Promedio=sum(Diccionario[i])
        Promedio=Promedio/len(Diccionario[i])
        LPromedios.append(Promedio)
        DesvEsta=stdev(Diccionario[i])
        LDesvEsta.append(DesvEsta)

    for j in range(len(Ataque)):
        Ataque[j]=(Ataque[j]-LPromedios[0])/LDesvEsta[0]
        Defensa[j] = (Defensa[j] - LPromedios[1]) / LDesvEsta[1]
        AtaqueEsp[j] = (AtaqueEsp[j] - LPromedios[2]) / LDesvEsta[2]
        DefensaEsp[j] = (DefensaEsp[j] - LPromedios[3]) / LDesvEsta[3]
        Velocidad[j] = (Velocidad[j] - LPromedios[4]) / LDesvEsta[4]

    print("NORMALIZACION\nAtaque: ",Ataque)
    print("\nNORMALIZACION\nDefensa: ",Defensa)
    print("\nNORMALIZACION\nAtaque Especial: ",AtaqueEsp)
    print("\nNORMALIZACION\nDefensa Especial: ",DefensaEsp)
    print("\nNORMALIZACION\nVelocidad: ",Velocidad)

estandarizacion(Dic)
