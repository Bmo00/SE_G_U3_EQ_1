import csv
import random
import sys
import statistics as s

import numpy as np
import serial as conecta

from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "Programa_1_Proyecto_MultipleSeleccion.py.ui"  # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

def resultado(r):
    with open("Resultados/ResultadosConfiguraciones.csv", "a") as d:
        d.write(f",{r}\n")

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.btn_accion.clicked.connect(self.accion)
        self.arduino = None

        self.btn_Enviar.clicked.connect(self.configurar)

        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.control)

        self.segundoPlano2 = QtCore.QTimer()
        self.segundoPlano2.timeout.connect(self.activar)
        self.segundoPlano2.start(10)

        self.res=""
        self.ConfigRes=""
        self.X=""

    def activar(self):
        if self.RdbN1.isChecked():
            self.cant = 1
            self.RdbMed.setEnabled(False)
            self.RdbMod.setEnabled(False)
            self.RdbProm.setEnabled(False)
            self.RdbMin.setEnabled(False)
            self.RdbMax.setEnabled(False)
            self.RdbNing.setEnabled(True)
        else:
            self.RdbMed.setEnabled(True)
            self.RdbMod.setEnabled(True)
            self.RdbProm.setEnabled(True)
            self.RdbMin.setEnabled(True)
            self.RdbMax.setEnabled(True)
            self.RdbNing.setEnabled(False)

        if self.RdbNing2.isChecked():
            self.RdbId3.setEnabled(False)
            self.RdbNbayes.setEnabled(False)
            self.RdbKnn.setEnabled(True)
            self.RdbAsc.setEnabled(True)
        else:
            self.RdbId3.setEnabled(True)
            self.RdbNbayes.setEnabled(True)
            self.RdbKnn.setEnabled(False)
            self.RdbAsc.setEnabled(False)

    def accion(self):
        try:
            if not self.txt_puerto.text() == "":
                txt_btn = self.btn_accion.text()
                if txt_btn == "CONECTAR": ##arduino == None
                    self.txt_estado.setText("CONECTADO")
                    self.btn_accion.setText("DESCONECTAR")
                    puerto = "COM" + self.txt_puerto.text()
                    self.arduino = conecta.Serial(puerto, baudrate=9600, timeout=1)
                    self.segundoPlano.start(100)
                elif txt_btn == "DESCONECTAR":
                    self.txt_estado.setText("DESCONECTADO")
                    self.btn_accion.setText("RECONECTAR")
                    self.segundoPlano.stop()
                else: #RECONECTAR
                    self.txt_estado.setText("RECONECTADO")
                    self.btn_accion.setText("DESCONECTAR")
                    puerto = "COM" + self.txt_puerto.text()
                    self.arduino = conecta.Serial(puerto, baudrate=9600, timeout=1)
                    self.segundoPlano.start(100)
        except Exception as error:
            print(error)

    def configurar(self):
        if self.RdbN30.isChecked():
            self.cant = 30
        elif self.RdbN50.isChecked():
            self.cant = 50
        elif self.RdbN100.isChecked():
            self.cant = 100

        if self.RdbMed.isChecked():
            metod = 'Mediana'
        elif self.RdbMod.isChecked():
            metod = 'Moda'
        elif self.RdbProm.isChecked():
            metod = 'Promedio'
        elif self.RdbMin.isChecked():
            metod = 'Minimo'
        elif self.RdbMax.isChecked():
            metod = 'Maximo'
        elif self.RdbNing.isChecked():
            metod = 'Ninguno'

        if self.RdbOutlier2.isChecked():
            Process2 = 'Cuartiles'
            if self.RdbEwb.isChecked():
                Process1 = 'EWB'
            elif self.RdbNing2.isChecked():
                Process1 = 'Ninguno'
        elif self.RdbOutlier3.isChecked():
            Process2 = 'EstadisticoZ'
            if self.RdbEwb.isChecked():
                Process1 = 'EWB'
            elif self.RdbNing2.isChecked():
                Process1 = 'Ninguno'
        else:
            if self.RdbEwb.isChecked():
                Process1 = 'EWB'
                Process2 = 'Nada'
            elif self.RdbNing2.isChecked():
                Process1 = 'Ninguno'
                Process2 = 'Nada'

        if self.RdbId3.isChecked():
            Alg = 'ID3'
        elif self.RdbKnn.isChecked():
            Alg = 'KNN'
        elif self.RdbNbayes.isChecked():
            Alg = 'NBayes'
        elif self.RdbAsc.isChecked():
            Alg = 'AsociadorL'

        rand = random.randint(100, 1000000)

        self.res = str(self.cant) + ',' + metod + "," + str(rand) + "," + Process1 + "," + Process2 + "," + Alg
        self.ConfigRes = str(self.cant) + ',' + metod + ',' + Process1 + ',' + Process2 + ',' + Alg

        with open("WConfiguración.csv", "w") as c:
            c.write(self.res)

    def control(self):
        if not self.arduino == None:
            if self.arduino.isOpen():
                # leer
                variable = self.arduino.readline().decode()
                variable = variable.replace("\r", "")
                variable = variable.replace("\n", "")
                #print(variable)

                if variable=="":

                    with open("WConfiguración.csv", "r") as r:
                        self.X = r.readline()

                    self.arduino.write(self.X.encode())

                    cadena = self.arduino.readline().decode()
                    cadena = cadena.replace("\r", "")
                    cadena = cadena.replace("\n", "")
                    cadena = cadena.split(",")

                    if len(cadena)==6:
                        cadena = np.array(cadena).reshape(1, len(cadena))

                        longitud=len(cadena[0])
                        if longitud==6:
                            print(cadena)

                            if (int(cadena[0][0]) >= 60 and int(cadena[0][0]) <= 79):
                                ValorAtributo1 = 1  # Simbolizando 1 como agua
                            elif (int(cadena[0][0]) >= 80 and int(cadena[0][0]) <= 100):
                                ValorAtributo1 = 2  # Simbolizando a 2 como fuego
                            elif (int(cadena[0][0]) >= 80 and int(cadena[0][0]) <= 89):
                                ValorAtributo1 = 3  # Simbolizando a 3 como planta
                            elif (int(cadena[0][0]) >= 70 and int(cadena[0][0]) <= 89):
                                ValorAtributo1 = 4  # Simbolizando a 4 como roca

                            if (int(cadena[0][1]) >= 60 and int(cadena[0][1]) <= 69):
                                ValorAtributo2 = 1  # Simbolizando 1 como agua
                            elif (int(cadena[0][1]) >= 85 and int(cadena[0][1]) <= 89):
                                ValorAtributo2 = 2  # Simbolizando a 2 como fuego
                            elif (int(cadena[0][1]) >= 70 and int(cadena[0][1]) <= 79):
                                ValorAtributo2 = 3  # Simbolizando a 3 como planta
                            elif (int(cadena[0][1]) >= 80 and int(cadena[0][1]) <= 100):
                                ValorAtributo2 = 4  # Simbolizando a 4 como roca

                            if (int(cadena[0][2]) >= 65 and int(cadena[0][2]) <= 79):
                                ValorAtributo3 = 1  # Simbolizando 1 como agua
                            elif (int(cadena[0][2]) >= 90 and int(cadena[0][2]) <= 100):
                                ValorAtributo3 = 2  # Simbolizando a 2 como fuego
                            elif (int(cadena[0][2]) >= 85 and int(cadena[0][2]) <= 89):
                                ValorAtributo3 = 3  # Simbolizando a 3 como planta
                            elif (int(cadena[0][2]) >= 75 and int(cadena[0][2]) <= 89):
                                ValorAtributo3 = 4  # Simbolizando a 4 como roca

                            if (int(cadena[0][3]) >= 80 and int(cadena[0][3]) <= 89):
                                ValorAtributo4 = 1  # Simbolizando 1 como agua
                            elif (int(cadena[0][3]) >= 90 and int(cadena[0][3]) <= 100):
                                ValorAtributo4 = 2  # Simbolizando a 2 como fuego
                            elif (int(cadena[0][3]) >= 65 and int(cadena[0][3]) <= 79):
                                ValorAtributo4 = 3  # Simbolizando a 3 como planta
                            elif (int(cadena[0][3]) >= 95 and int(cadena[0][3]) <= 100):
                                ValorAtributo4 = 4  # Simbolizando a 4 como roca

                            if (int(cadena[0][4]) >= 70 and int(cadena[0][4]) <= 89):
                                ValorAtributo5 = 1  # Simbolizando 1 como agua
                            elif (int(cadena[0][4]) >= 60 and int(cadena[0][4]) <= 79):
                                ValorAtributo5 = 2  # Simbolizando a 2 como fuego
                            elif (int(cadena[0][4]) >= 50 and int(cadena[0][4]) <= 69):
                                ValorAtributo5 = 3  # Simbolizando a 3 como planta
                            elif (int(cadena[0][4]) >= 20 and int(cadena[0][4]) <= 49):
                                ValorAtributo5 = 4
                            elif not (int(cadena[0][4]) >= 20 and int(cadena[0][4]) <= 49):
                                ValorAtributo5 = 4

                            vector = [ValorAtributo1,ValorAtributo2,ValorAtributo3,ValorAtributo4,ValorAtributo5]

                            asclinear = [0]*12
                            asclinear[0]=1
                            asclinear[1]=5
                            asclinear[2]=4
                            contador=-1
                            for asd in range(3,8):
                                contador+=1
                                asclinear[asd]=(cadena[0][contador])

                            res = s.multimode(vector)
                            if len(res) == 2:
                                # print(s.mode(vector))
                                index = random.randint(0, 1)
                                clase = res[index]
                                print(clase)
                            else:
                                clase = res[0]
                                print(clase)

                            if (clase == 1):
                                cadena[0][5]="agua"
                                asclinear[8] = 0
                                asclinear[9] = 0
                                asclinear[10] = 0
                                asclinear[11] = 1
                            elif (clase == 2):
                                cadena[0][5]="fuego"
                                asclinear[8] = 0
                                asclinear[9] = 0
                                asclinear[10] = 1
                                asclinear[11] = 0
                            elif (clase == 3):
                                cadena[0][5]="plant"
                                asclinear[8] = 0
                                asclinear[9] = 1
                                asclinear[10] = 0
                                asclinear[11] = 0
                            elif (clase == 4):
                                cadena[0][5]="roca"
                                asclinear[8] = 1
                                asclinear[9] = 0
                                asclinear[10] = 0
                                asclinear[11] = 0

                            self.arduino.write(str(clase).encode())

                            asclinear = np.array(asclinear).reshape(1, len(asclinear))
                            asclinear=np.transpose(asclinear)

                            x=self.X.split(",")

                            cadenaCabecera = [[0] * (len(cadena[0])) for i in range(len(cadena)+1)]

                            for fila in range(len(cadena[0])):
                                cadenaCabecera[1][fila]=cadena[0][fila]

                            cadenaCabecera[0][0]="Atr1";cadenaCabecera[0][1]="Atr2";cadenaCabecera[0][2]="Atr3"
                            cadenaCabecera[0][3] = "Atr4";cadenaCabecera[0][4]="Atr5";cadenaCabecera[0][5]="Clase"

                            with open(f'YResultadoTest.csv', 'w', newline='') as file:
                                mywriter = csv.writer(file, delimiter=',')
                                mywriter.writerows(cadena)

                            with open(f'YResultadoTestConCabecera.csv', 'w', newline='') as file:
                                mywriter = csv.writer(file, delimiter=',')
                                mywriter.writerows(cadenaCabecera)

                            with open(f'YResultadoTestInvertido.txt', 'w', newline='') as file:
                                mywriter = csv.writer(file, delimiter='\t')
                                mywriter.writerows(asclinear)

                            # with open("Resultados/ResultadosConfiguraciones.csv", "a") as d:
                            #     d.write(self.ConfigRes)

                            long=6

                            ####SENTENCIAS PARA HACER IAS
                            if x[4]=="Cuartiles":
                                print("\nEVALUANDO OUTLIER X CUARTILES...")
                                import OutliersXLongitud
                                long = OutliersXLongitud.LongitudFinalXQuartiles()
                                del sys.modules['OutliersXLongitud']
                            elif x[4]=="EstadisticoZ":
                                print("\nEVALUANDO OUTLIER X ESTADISTICOZ...")
                                import OutliersXLongitud
                                long = OutliersXLongitud.LongitudFinalXEstadisticoZ()
                                del sys.modules['OutliersXLongitud']

                            if long==6:
                                print("\nNO HAY OUTLIERS...\nPROCEDIENDO CON LA IA...\n")
                                if x[3]=="EWB":
                                    import Programa_EWB
                                    del sys.modules['Programa_EWB']
                                    if x[5] == "ID3":
                                        import ID3Main
                                        Result=ID3Main.Resultado()
                                        resultado(Result)
                                        del sys.modules['ID3Main']
                                    elif x[5]=="NBayes":
                                        import NaiveBayes
                                        Result = NaiveBayes.Resultado()
                                        resultado(Result)
                                        del sys.modules['NaiveBayes']
                                elif x[3]=="Ninguno":
                                    if x[5]=="KNN":
                                        import KNN_Pokemones
                                        Result = KNN_Pokemones.Resultado()
                                        resultado(Result)
                                        del sys.modules['KNN_Pokemones']
                                    elif x[5]=="AsociadorL":
                                        import AsociadorLineal
                                        Result = AsociadorLineal.Resultado()
                                        resultado(Result)
                                        del sys.modules['AsociadorLineal']
                            else:
                                print("\nEL SISTEMA DETECTO OULIERS...\nFIN DE LA CONFIGURACION")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())