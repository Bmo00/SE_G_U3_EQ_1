import pandas as pd
Datos = pd.read_csv("../Archivos/Pokemones.csv", sep=',') #ALMACENAR EL DATASET EN LA VARIABLE DATOS
Ataque,Defensa,AtaqueEsp,DefensaEsp,Velocidad = Datos["Ataque"],Datos["Defensa"],Datos["AtqEsp"],Datos["DefEsp"],Datos["Velocidad"]
#LO DE ARRIBA LO QUE HACE ES OBTENER SOLO LA COLUMNA CON EL NOMBRE DADO, 5 VARIABLES 5 COLUMNAS

Ataque = Ataque.to_list()#ESTO CONVIERTE LOS VALORES DE LA COLUMNA ATAQUE A LISTA Y LO MISMO CON LOS DEMAS
Defensa = Defensa.to_list()
AtaqueEsp = AtaqueEsp.to_list()
DefensaEsp = DefensaEsp.to_list()
Velocidad = Velocidad.to_list()

def Cuartiles(lista):
    n=len(lista)
    q1 = 1*(n+1)/4 -1
    if isinstance(q1, float):
        q1 = lista[int(q1)] + q1%1 * (lista[int(q1+1)] - lista[int(q1)])
    else:
        q1=lista[q1]
    q2 = 2*(n+1)/4 -1
    if isinstance(q2, float):
        q2 = lista[int(q2)] + q2%1 * (lista[int(q2+1)] - lista[int(q2)])
    else:
        q2=lista[q2]
    q3 = 3*(n+1)/4 -1
    if isinstance(q3, float):
        q3 = lista[int(q3)] + q3%1 * (lista[int(q3+1)] - lista[int(q3)])
    else:
        q3=lista[q3]
    return q1, q2, q3

def Outliers_Suave(Q1,Q3,IQR,lista):
    min_val = Q1 - (1.5 * IQR)
    max_val = Q3 + (1.5 * IQR)
    outliers = [x for x in lista if x < min_val or x > max_val]
    return min_val,max_val,outliers

def Outliers_Extremo(Q1,Q3,IQR,lista):
    min_val = Q1- (3.0 * IQR)
    max_val = Q3+ (3.0 * IQR)
    outliers = [x for x in lista if x < min_val or x > max_val]
    return min_val,max_val,outliers

print("ATAQUE:")#LISTA ATAQUE
print("Ataque Original: ",Ataque)
Ataque.sort()
print("Ataque Ordenada: ",Ataque)
Q1, Q2, Q3 = Cuartiles(Ataque)
IQR=Q3-Q1
min_s,max_s,suave=Outliers_Suave(Q1,Q3,IQR,Ataque)
min_e,max_e,extremo=Outliers_Extremo(Q1,Q3,IQR,Ataque)
print("Q1: ",Q1)
print("Q2: ",Q2)
print("Q3: ",Q3)
print("IQR: ",IQR)
print("Min suave: ",min_s, "Max suave: ",max_s)
print("Min extremo: ",min_e, "Max extremo: ",max_e)
print("Outliers Suave: ", suave)
print("Outliers extremo: ",extremo)
print("")

print("DEFENSA:")#LISTA DEFENSA
print("Defensa Original: ",Defensa)
Defensa.sort()
print("Defensa Ordenada: ",Defensa)
Q1, Q2, Q3 = Cuartiles(Defensa)
IQR=Q3-Q1
min_s,max_s,suave=Outliers_Suave(Q1,Q3,IQR,Defensa)
min_e,max_e,extremo=Outliers_Extremo(Q1,Q3,IQR,Defensa)
print("Q1: ",Q1)
print("Q2: ",Q2)
print("Q3: ",Q3)
print("IQR: ",IQR)
print("Min suave: ",min_s, "Max suave: ",max_s)
print("Min extremo: ",min_e, "Max extremo: ",max_e)
print("Outliers Suave: ", suave)
print("Outliers extremo: ",extremo)
print("")

print("ATAQUEESP:")#LISTA ATAQUE ESPECIAL
print("AtaqueEsp Original: ",AtaqueEsp)
AtaqueEsp.sort()
print("AtaqueEsp Ordenada: ",AtaqueEsp)
Q1, Q2, Q3 = Cuartiles(AtaqueEsp)
IQR=Q3-Q1
min_s,max_s,suave=Outliers_Suave(Q1,Q3,IQR,AtaqueEsp)
min_e,max_e,extremo=Outliers_Extremo(Q1,Q3,IQR,AtaqueEsp)
print("Q1: ",Q1)
print("Q2: ",Q2)
print("Q3: ",Q3)
print("IQR: ",IQR)
print("Min suave: ",min_s, "Max suave: ",max_s)
print("Min extremo: ",min_e, "Max extremo: ",max_e)
print("Outliers Suave: ", suave)
print("Outliers extremo: ",extremo)
print("")
print("")

print("DEFENSAESP:")#LISTA DEFENSA ESPECIAL
print("DefensaEsp Original: ",DefensaEsp)
DefensaEsp.sort()
print("DefensaEsp Ordenada: ",DefensaEsp)
Q1, Q2, Q3 = Cuartiles(DefensaEsp)
IQR=Q3-Q1
min_s,max_s,suave=Outliers_Suave(Q1,Q3,IQR,DefensaEsp)
min_e,max_e,extremo=Outliers_Extremo(Q1,Q3,IQR,DefensaEsp)
print("Q1: ",Q1)
print("Q2: ",Q2)
print("Q3: ",Q3)
print("IQR: ",IQR)
print("Min suave: ",min_s, "Max suave: ",max_s)
print("Min extremo: ",min_e, "Max extremo: ",max_e)
print("Outliers Suave: ", suave)
print("Outliers extremo: ",extremo)
print("")
print("")

print("VELOCIDAD:")#LISTA VELOCIDAD
print("Velocidad Original: ",Velocidad)
Velocidad.sort()
print("Velocidad Ordenada: ",Velocidad)
Q1, Q2, Q3 = Cuartiles(Velocidad)
IQR=Q3-Q1
min_s,max_s,suave=Outliers_Suave(Q1,Q3,IQR,Velocidad)
min_e,max_e,extremo=Outliers_Extremo(Q1,Q3,IQR,Velocidad)
print("Q1: ",Q1)
print("Q2: ",Q2)
print("Q3: ",Q3)
print("IQR: ",IQR)
print("Min suave: ",min_s, "Max suave: ",max_s)
print("Min extremo: ",min_e, "Max extremo: ",max_e)
print("Outliers Suave: ", suave)
print("Outliers extremo: ",extremo)
print("")