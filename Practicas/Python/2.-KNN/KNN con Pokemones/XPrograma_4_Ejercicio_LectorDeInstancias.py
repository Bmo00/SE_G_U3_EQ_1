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
        self.Mat=[]

    # Área de los Slots
    def Crear(self):
        CAtributos=5
        nombre=self.txt_instancia.text()#Obtiene el nombre de la instancia a separar y lo pone en la ruta
        totElementos=self.txt_elementos.text()#Obtiene total de elementos a leer de la instancia maximo=49 elementos
        train = self.txt_train.text() #Obtiene el total de elementos de entrenamiento(es de ley que siempre debe ser
                                    #mas que los elementos de prueba por eso mas adelante hay condiciones que evaluan eso.

        if not nombre=="" and not totElementos=="" and not train=="": #evalua que los line edits no esten vacios
            totElementos = int(totElementos)
            train=int(train)
            Datos = pd.read_csv(f"{nombre}.csv", sep=',') #almacena en Datos el csv con ayuda de pandas

            for d in range(CAtributos):
                self.Mat.append(Datos[f"Atr{d + 1}"])#El archivo a leer debe estar renombrado por Atr1, Atr2 etc
                                                    #es decir ya no es Ataque ahora para mayor comodidad es Atr1, y asi
                                                    #Y Genera una lista con todas esas columnas para despues
                                                    #transformar esa lista a una tipo Matriz

            self.Mat.append(Datos["Clase"])#En el for anterior agarra solo los atributos y este lo que hace es agarrar
                                        #El atributo llamado clase, es decir la ultima columna(planta,roca,etc)
            self.Mat = np.array(self.Mat).reshape(CAtributos + 1, len(self.Mat[0]))#Convierte a una tipo matriz la lista
            MReal = [[0] * (CAtributos + 1) for i in range(len(self.Mat[0]))]#Se inicializa con puros ceros una matriz
            #Ya que en python para usar una matriz debes inicializarla

            for z in range(len(self.Mat[0])):
                for x in range(CAtributos + 1):
                    MReal[z][x] = self.Mat[x][z]#Pasas esa matriz a la matriz real por problemas presentados con la
                    #Anterior y esta fue al primera solucion que se vino en mente

            if train>totElementos or totElementos>len(Datos): # evalua que no exceda el total de elementos dados
                self.txt_titulo.setText(f"HA EXCEDIDO LA CANTIDAD DE ELEMENTOS")
            else:
                test=totElementos-train #Operacion para sacar los datos de prueba(por eso en la interfaz esta bloqueado
                                        #su line edit, se saca la cantidad de prueba automaticamente
                self.txt_test.setText(str(test))

                MTrain = [[0] * len(MReal[0]) for i in range(train)] #Lo mismo inicializa matriz mtrain y mtest
                MTest = [[0] * len(MReal[0]) for i in range(test)]
                # Estas matrices son los que contendran los datos de prueba y entrenamiento, es decir aqui se almacenara el dataset separado

                ran=random.sample(range(0,len(MReal)),totElementos) #El ejercicio trata de que los datos a separar salgan de manera aleatoria
                #Esta forma es obtener numeros random sin que se repitan, ran pasara a ser una lista de randoms
                #(0,len(M)= de donde a donde, como si pusieras un random.randint(0,len(M)), y ,totElementos=Tamaño de la lista a crear

                for i in range(train):
                    for j in range(len(MReal[0])):
                        MTrain[i][j]=MReal[ran[i]][j]#Aqui solo esta almacenando los indices random obtenidos a la matriz Mtrain
                        # inicializada anteriormente ran[i]=indice ejemplo ran[4,2,7,8]...ran[i]=4 entonces matriz posicion [4][j]

                indice=train #como ran obtuvo numeros random en una sola lista se especifica a indice que empiece en la posicion
                #de train para que sepa en que indice de la lista llamada ran debe seguir para los datos de prueba
                #Ejemplo: totelementos=10 y train=7 entonces solo sobran 3 para test y la lista randon es:
                # ran[4,5,7,9,1,3,8,0,2,6] entonces las primeras 7 filas son para train(entrenamiento) 4,5,6,9,1,3,8,0,2,6 e indice=train
                #entonces para prueba(MTest) empezara desde el indice 7 de la lista ran es decir las filas para test son: 0,2 y 6
                for i in range(test):
                    for j in range(len(MReal[0])):
                        MTest[i][j]=MReal[ran[indice]][j]
                    indice+=1

                print(MTrain)
                print(MTest)#imprimir y lo de abajo es para mandar a .csv una matriz

                with open('XPokemones_Training.csv', 'w', newline='') as file:
                    mywriter = csv.writer(file, delimiter=',')
                    mywriter.writerows(MTrain)

                with open('XPokemones_Test.csv', 'w', newline='') as file:
                    mywriter = csv.writer(file, delimiter=',')
                    mywriter.writerows(MTest)

                self.txt_titulo.setText(f"PROCESO CREADO EXITOSAMENTE ! !")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())