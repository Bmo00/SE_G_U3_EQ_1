import csv
import sys
import random
import numpy as np
import pandas as pd
from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "XPrograma_4_Ejercicio_LectorDeInstancias.ui"  # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_crear.clicked.connect(self.Crear)
        self.txt_test.setEnabled(False)

    # Área de los Slots
    def Crear(self):
        nombre=self.txt_instancia.text()#Obtiene el nombre de la instancia a separar y lo pone en la ruta
        totElementos=self.txt_elementos.text()#Obtiene total de elementos a leer de la instancia maximo=49 elementos
        train = self.txt_train.text() #Obtiene el total de elementos de entrenamiento(es de ley que siempre debe ser
                                    #mas que los elementos de prueba por eso mas adelante hay condiciones que evaluan eso.

        if not nombre=="" and not totElementos=="" and not train=="": #evalua que los line edits no esten vacios
            totElementos = int(totElementos)
            train=int(train)
            Datos = pd.read_csv(f"{nombre}.csv", sep=',') #almacena en Datos el csv con ayuda de pandas
            if train>totElementos or totElementos>len(Datos): # evalua que no exceda el total de elementos dados
                self.txt_titulo.setText(f"HA EXCEDIDO LA CANTIDAD DE ELEMENTOS")
            else:
                test=totElementos-train #Operacion para sacar los datos de prueba(por eso en la interfaz esta bloqueado
                                        #su line edit, se saca la cantidad de prueba automaticamente
                self.txt_test.setText(str(test))
                M = np.array(Datos).reshape(len(Datos),len(Datos.columns))#Operacion para crear una matriz con numpy ya que
                                                                        #"Datos" no es una matriz, es una lista

                MTrain = [[0] * (len(M[0])) for i in range(train)] #Operacion para inicializar una matriz. Es una lista de comprension
                MTest = [[0] * (len(M[0])) for i in range(test)]
                # Estas matrices son los que contendran los datos de prueba y entrenamiento, es decir aqui se almacenara el dataset separado

                ran=random.sample(range(0,len(M)),totElementos) #El ejercicio trata de que los datos a separar salgan de manera aleatoria
                #Esta forma es obtener numeros random sin que se repitan, ran pasara a ser una lista de randoms
                #(0,len(M)= de donde a donde, como si pusieras un random.randint(0,len(M)), y ,totElementos=Tamaño de la lista a crear

                for i in range(train):
                    for j in range(len(M[0])):
                        MTrain[i][j]=M[ran[i]][j]#Aqui solo esta almacenando los indices random obtenidos a la matriz Mtrain
                        # inicializada anteriormente ran[i]=indice ejemplo ran[4,2,7,8]...ran[i]=4 entonces matriz posicion [4][j]

                indice=train #como ran obtuvo numeros random en una sola lista se especifica a indice que empiece en la posicion
                #de train para que sepa en que indice de la lista llamada ran debe seguir para los datos de prueba
                #Ejemplo: totelementos=10 y train=7 entonces solo sobran 3 para test y la lista randon es:
                # ran[4,5,7,9,1,3,8,0,2,6] entonces las primeras 7 filas son para train(entrenamiento) 4,5,6,9,1,3,8,0,2,6 e indice=train
                #entonces para prueba(MTest) empezara desde el indice 7 de la lista ran es decir las filas para test son: 0,2 y 6
                for i in range(test):
                    for j in range(len(M[0])):
                        MTest[i][j]=M[ran[indice]][j]
                    indice+=1

                MTrain=np.transpose(MTrain)#COMO TODO EL ALGORITMO ES EL MISMO LO UNICO NUEVO ES ESTO, SOLO SE TRANSPONE
                MTest = np.transpose(MTest)

                print(MTrain)
                print(MTest)#imprimir y lo de abajo es para mandar a .csv una matriz

                with open('XIris_Training.txt', 'w', newline='') as file:
                    mywriter = csv.writer(file, delimiter='\t')#AQUI LO UNICO QUE SE HACE ES SUSTITUIR EL , POR \t
                    #PARA ALAMACENAR EN EL TXT LA MATRIZ TABULADA Y ALINEADA
                    mywriter.writerows(MTrain)

                with open('XIris_Test.txt', 'w', newline='') as file:
                    mywriter = csv.writer(file, delimiter='\t')#LO MISMO
                    mywriter.writerows(MTest)

                self.txt_titulo.setText(f"PROCESO CREADO EXITOSAMENTE ! !")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())