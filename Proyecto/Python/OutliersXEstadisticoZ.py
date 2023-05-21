import pandas as pd
import numpy as np
from scipy import stats

Train = pd.read_csv("XPokemones_TrainingSinEWB.csv", sep=',')
matriz_Train = np.array(Train).reshape(140, 6)
listas_columnas = [*matriz_Train.T.tolist()]
Ataque = listas_columnas[0]
Defensa = listas_columnas[1]
AtaqueEsp = listas_columnas[2]
DefensaEsp = listas_columnas[3]
Velocidad = listas_columnas[4]

Test = pd.read_csv("YResultadoTestConCabecera.csv", sep=',')
matriz_Test = np.array(Test).reshape(1, 6)
listas_columnasTest = [*matriz_Test.T.tolist()]
AtaqueTest = listas_columnasTest[0]
DefensaTest = listas_columnasTest[1]
AtaqueEspTest = listas_columnasTest[2]
DefensaEspTest = listas_columnasTest[3]
VelocidadTest = listas_columnasTest[4]
clase=listas_columnasTest[5]

def detectar_outliers_zscore(datos, umbral=3):
    z_scores = np.abs(stats.zscore(datos))
    indices_outliers = np.where(z_scores > umbral)[0]
    return indices_outliers

# Detectar outliers en el Train
outliers_Ataque = detectar_outliers_zscore(Ataque)
outliers_Defensa = detectar_outliers_zscore(Defensa)
outliers_AtaqueEsp = detectar_outliers_zscore(AtaqueEsp)
outliers_DefensaEsp = detectar_outliers_zscore(DefensaEsp)
outliers_Velocidad = detectar_outliers_zscore(Velocidad)

# Calcular el Estadistico Z para Test
print("ATAQUE:")#LISTA ATAQUE
AtaqueTest_z = np.abs((AtaqueTest - np.mean(Ataque)) / np.std(Ataque))
if AtaqueTest_z > 3:
    print(AtaqueTest_z)
    print(AtaqueTest)
    AtaqueTest.pop(0)
    print(AtaqueTest)
else:
    print("No hay Outliers")

print("DEFENSA:")#LISTA DEFENSA
DefensaTest_z = np.abs((DefensaTest - np.mean(Defensa)) / np.std(Defensa))
if DefensaTest_z > 3:
    print(DefensaTest_z)
    print(DefensaTest)
    DefensaTest.pop(0)
    print(DefensaTest)
else:
    print("No hay Outliers")

print("ATAQUEESP:")#LISTA ATAQUE ESPECIAL
AtaqueEspTest_z = np.abs((AtaqueEspTest - np.mean(AtaqueEsp)) / np.std(AtaqueEsp))
if AtaqueEspTest_z > 3:
    print(AtaqueEspTest_z)
    print(AtaqueEspTest)
    AtaqueEspTest.pop(0)
    print(AtaqueEspTest)
else:
    print("No hay Outliers")

print("DEFENSAESP:")#LISTA DEFENSA ESPECIAL
DefensaEspTest_z =  np.abs((DefensaEspTest - np.mean(DefensaEsp)) / np.std(DefensaEsp))
if DefensaEspTest_z > 3:
    print(DefensaEspTest_z)
    print(DefensaEspTest)
    DefensaEspTest.pop(0)
    print(DefensaEspTest)
else:
    print("No hay Outliers")


print("VELOCIDAD:")#LISTA VELOCIDAD
VelocidadTest_z = np.abs((VelocidadTest - np.mean(Velocidad)) / np.std(Velocidad))
if VelocidadTest_z > 3:
    print(VelocidadTest_z)
    print(VelocidadTest)
    VelocidadTest.pop(0)
    print(VelocidadTest)
else:
    print("No hay Outliers")
print("")

lista_final= AtaqueTest + DefensaTest + AtaqueEspTest + DefensaEspTest + VelocidadTest + clase
print(lista_final)

def Final():
    lista_final= AtaqueTest + DefensaTest + AtaqueEspTest + DefensaEspTest + VelocidadTest + clase
    return lista_final