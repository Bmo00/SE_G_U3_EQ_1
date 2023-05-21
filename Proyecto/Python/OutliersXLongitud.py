import sys


def LongitudFinalXQuartiles():
    import OutliersXQuartiles
    lista_final = OutliersXQuartiles.Final()
    longitud_lista_final = len(lista_final)
    print("Longitud final:",longitud_lista_final)
    del sys.modules['OutliersXQuartiles']
    return longitud_lista_final


def LongitudFinalXEstadisticoZ():
    import OutliersXEstadisticoZ
    lista_final = OutliersXEstadisticoZ.Final()
    longitud_lista_final = len(lista_final)
    print("Longitud final:",longitud_lista_final)
    del sys.modules['OutliersXEstadisticoZ']
    return longitud_lista_final


