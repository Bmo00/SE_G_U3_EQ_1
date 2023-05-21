import pandas as pd
import numpy as np

Train = pd.read_csv("XPokemones_TrainingSinEWB.csv", sep=',')
matriz_Train = np.array(Train).reshape(140, 6)
listas_columnas = [*matriz_Train.T.tolist()]
Ataque = listas_columnas[0]
Defensa = listas_columnas[1]
AtaqueEsp = listas_columnas[2]
DefensaEsp = listas_columnas[3]
Velocidad = listas_columnas[4]

Test = pd.read_csv("YResultadoTestConCabecera.csv", sep=',')
matriz_Test = np.array(Test).reshape(1,6)
listas_columnasTest = [*matriz_Test.T.tolist()]
AtaqueTest = listas_columnasTest[0]
DefensaTest = listas_columnasTest[1]
AtaqueEspTest = listas_columnasTest[2]
DefensaEspTest = listas_columnasTest[3]
VelocidadTest = listas_columnasTest[4]
clase=listas_columnasTest[5]

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
min_s,max_s,suave=Outliers_Suave(Q1,Q3,IQR,AtaqueTest)#Aqui en lugar de meter la lista original Ataque con la que se calculó
min_e,max_e,extremo=Outliers_Extremo(Q1,Q3,IQR,AtaqueTest)#Los cuartiles, se pone la lista del TEST el vector de Arduino

if len(suave) > 0 or len(extremo) > 0:
    AtaqueTest.pop(0)
else:
    print("No hay Outliers")
print("")

print("DEFENSA:")#LISTA DEFENSA
print("Defensa Original: ",Defensa)
Defensa.sort()
print("Defensa Ordenada: ",Defensa)
Q1, Q2, Q3 = Cuartiles(Defensa)
IQR=Q3-Q1
min_s,max_s,suave=Outliers_Suave(Q1,Q3,IQR,DefensaTest)
min_e,max_e,extremo=Outliers_Extremo(Q1,Q3,IQR,DefensaTest)

if len(suave) > 0 or len(extremo) > 0:
    DefensaTest.pop(0)
else:
    print("No hay Outliers")
print("")

print("ATAQUEESP:")#LISTA ATAQUE ESPECIAL
print("AtaqueEsp Original: ",AtaqueEsp)
AtaqueEsp.sort()
print("AtaqueEsp Ordenada: ",AtaqueEsp)
Q1, Q2, Q3 = Cuartiles(AtaqueEsp)
IQR=Q3-Q1
min_s,max_s,suave=Outliers_Suave(Q1,Q3,IQR,AtaqueEspTest)
min_e,max_e,extremo=Outliers_Extremo(Q1,Q3,IQR,AtaqueEspTest)

if len(suave) > 0 or len(extremo) > 0:
    AtaqueEspTest.pop(0)
else:
    print("No hay Outliers")
print("")

print("DEFENSAESP:")#LISTA DEFENSA ESPECIAL
print("DefensaEsp Original: ",DefensaEsp)
DefensaEsp.sort()
print("DefensaEsp Ordenada: ",DefensaEsp)
Q1, Q2, Q3 = Cuartiles(DefensaEsp)
IQR=Q3-Q1
min_s,max_s,suave=Outliers_Suave(Q1,Q3,IQR,DefensaEspTest)
min_e,max_e,extremo=Outliers_Extremo(Q1,Q3,IQR,DefensaEspTest)

if len(suave) > 0 or len(extremo) > 0:
    DefensaEspTest.pop(0)
else:
    print("No hay Outliers")
print("")

print("VELOCIDAD:")#LISTA VELOCIDAD
print("Velocidad Original: ",Velocidad)
Velocidad.sort()
print("Velocidad Ordenada: ",Velocidad)
Q1, Q2, Q3 = Cuartiles(Velocidad)
IQR=Q3-Q1
min_s,max_s,suave=Outliers_Suave(Q1,Q3,IQR,VelocidadTest)
min_e,max_e,extremo=Outliers_Extremo(Q1,Q3,IQR,VelocidadTest)

if len(suave) > 0 or len(extremo) > 0:
    VelocidadTest.pop(0)
else:
    print("No hay Outliers")
print("")

lista_final= AtaqueTest + DefensaTest + AtaqueEspTest + DefensaEspTest + VelocidadTest + clase
print(lista_final)

def Final():
    lista_final= AtaqueTest + DefensaTest + AtaqueEspTest + DefensaEspTest + VelocidadTest + clase
    return lista_final