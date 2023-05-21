from statistics import stdev
import numpy as np
import pandas as pd

LPromedios = []
LDesvEsta = []
Datos = pd.read_csv("../Archivos/Dataset Pokemones.csv", sep=',')
print(Datos)# ALMACENAR EL DATASET EN LA VARIABLE DATOS

Ataque, Defensa, AtaqueEsp, DefensaEsp, Velocidad = Datos["Ataque"], Datos["Defensa"], Datos["AtqEsp"], Datos["DefEsp"], \
Datos["Velocidad"]
# LO DE ARRIBA LO QUE HACE ES OBTENER SOLO LA COLUMNA CON EL NOMBRE DADO, 5 VARIABLES 5 COLUMNAS

Ataque = Ataque.to_list()  # ESTO CONVIERTE LOS VALORES DE LA COLUMNA ATAQUE A LISTA Y LO MISMO CON LOS DEMAS
Defensa = Defensa.to_list()
AtaqueEsp = AtaqueEsp.to_list()
DefensaEsp = DefensaEsp.to_list()
Velocidad = Velocidad.to_list()
print(Ataque)
Dic = {"Atq": Ataque, "Def": Defensa, "AtqEsp": AtaqueEsp, "DefEsp": DefensaEsp, "Velocidad": Velocidad}
# LO DE ARRIBA ES UN DICCIONARIO DE LISTAS

lisfull = Ataque + Defensa + AtaqueEsp + DefensaEsp + Velocidad
print(lisfull)
minimo = np.min(lisfull)
maximo = np.max(lisfull)

print('minimo=', minimo)
# print(LPromedios)
# print(LDesvEsta)

def normalizacion(atk,defe,atksp,defsp,vel):
    for j in range(len(Ataque)):
        atk[j] = (atk[j] - minimo) / (maximo - minimo)
        defe[j] = (defe[j] - minimo) / (maximo - minimo)
        atksp[j] = (atksp[j] - minimo) / (maximo - minimo)
        defsp[j] = (defsp[j] - minimo) / (maximo - minimo)
        vel[j] = (vel[j] - minimo) / (maximo - minimo)
    return Ataque,Defensa,AtaqueEsp,DefensaEsp,Velocidad

normalizacion(Ataque,Defensa,AtaqueEsp,DefensaEsp,Velocidad)
print("NORMALIZACION\nAtaque: ", Ataque)
print("\nNORMALIZACION\nDefensa: ", Defensa)
print("\nNORMALIZACION\nAtaque Especial: ", AtaqueEsp)
print("\nNORMALIZACION\nDefensa Especial: ", DefensaEsp)
print("\nNORMALIZACION\nVelocidad: ", Velocidad)
