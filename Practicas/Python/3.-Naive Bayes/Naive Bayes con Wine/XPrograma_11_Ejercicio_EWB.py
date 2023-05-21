import csv
import numpy as np
import pandas as pd

Mds=[];PM=[];SM=[];LA=[];Mat=[]
CAtributos=13
Dic={}
Datos = pd.read_csv("wine.csv", sep=',')

for d in range(CAtributos): ######NUEVA FORMA DE LEER LOS ATRIBUTOS DEL DATASET, RENOMBRAR A (Atr1,Atr2,etc) es para mayor comodidad
    Mat.append(Datos[f"Atr{d+1}"])#Agrega todas las columas a una lista llamado MAT dependiendo el total de atributos
    Atr=Datos[f"Atr{d+1}"]#Este lo que hace es obtener la primera columna para despues mandarlo a un diccionario
    Key=f"Atr{d+1}"#Este lo que hace es obtener el nombre de cada atributo, en este caso Atr,Atr2,Atr3 etc
    Value=Atr.to_list()#Aqui se convierte el primer atributo a lista y ahora Value contiene esa lista
    Dic[Key]=Value#Esta es la sintaxis para agregar dinamicamente una llave con sus datos al diccionario,Ej.Atr1:[1,2,3,4,...]

Mat.append(Datos["Clase"])#ESTE HARA QUE AGARRE EL ATRIBUTO LLAMADO CLASE, AHI PUEDEN VER EL EJEMPLO DE LOS POKES como estan renombrados

Mat = np.array(Mat).reshape(CAtributos+1,len(Mat[0]))#Convierte a una tipo matriz la lista llamado MAT
MReal = [[0] * (CAtributos+1) for i in range(len(Mat[0]))]#Se inicializa una matriz ya que en python para usar
#matrices primero se deben inicializar

for z in range(len(Mat[0])):
    for x in range(CAtributos+1):
        MReal[z][x]=Mat[x][z] #Se pasa la tipo matriz a la matriz real

def EWB(diccionario,K,generar=False): #Se manda como parametro el diccionario, el total de k y si se quiere o no
                                    #generar el archivo .csv discretizado
    c = 0
    for i in diccionario:
        maximo=max(diccionario[i])
        minimo = min(diccionario[i])
        width=(maximo-minimo)/K #Todo esto es para sacar width siguiendo la formula del profe
        print(i) #Este solo es un identificador al momento de imprimir

        print("\nWidth: ",width)
        print("Maximo: ", maximo)
        for j in range(K):
            L1=minimo+j*width #igualmente siguiendo la formula del profe se saca el valor 1
            L2=minimo+(j+1)*width #y aqui el valor 2 ejemplo del pizarron (1 , 30.5) siguiente iteracion (30.5 , 61) etc
            print("(",L1,",",L2,")")

            for f in range(len(Datos)):
                if MReal[f][c]>=L1 and MReal[f][c]<=L2:
                    MReal[f][c]=int(f"{j+1}")#Esto lo que hace es comparar si en la primera iteracion que datos son V1, es decir
                    #que datos estan en el rango del primer resultado(ejemplo pizarron mayores a 1 y menores a 30.5
                    #A esos valores que encuentre le asignara el valor "1" el profe le puso "V1" y en la segunda iteracion
                    #Hara lo mismo hasta k veces por cada columna asignandole "1" o "2" o "3" dependiendo cuantos k fueron

        c += 1
    print("\n",MReal,"\n")

    if(generar==True): #Generar el dataset pero primero evaluara que se le haya dicho que si
        with open('XWine_Discretizado.csv', 'w', newline='') as file:
            mywriter = csv.writer(file, delimiter=',')
            mywriter.writerows(MReal)

        print("ARCHIVO GENERADO CON EXITO")

EWB(diccionario=Dic,K=6,generar=True) #Este es el que controlara ya saben se mandan los parametros por aqui