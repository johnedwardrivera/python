#NO ELIMINAR LAS SIGUIENTES IMPORTACIONES, sirven para probar tu código en consola, y el funcionamiento del módulo csv respectivamente
from pruebas import pruebas_codigo_estudiante
import csv
"""NOTAS: 
    -PARA ESTE RETO PUEDES PROBAR TU PROGRAMA, DANDO CLICK EN LA NAVE ESPACIAL
    -LA CONSOLA TE DARÁ INSTRUCCIONES SI PUEDES EVALUAR O NO TU CÓDIGO
"""


"""Inicio espacio para programar funciones propias"""
#En este espacio podrás programar las funciones que deseas usar en la función solución (ES OPCIONAL)



"""Fin espacio para programar funciones propias"""

def solucion():
    #ESTA ES LA FUNCIÓN A LA QUE LE DEBES GARANTIZAR LOS RETORNOS REQUERIDOS EN EL ENUNCIADO. 
    listAnalisis=[]
    listprecioBajo=[]
    listprecioAlto=[]
    with open('TSLA.csv',newline='') as File: 
        reader=csv.reader(File)
        next(reader,None)
        for row in reader:
            if row[4] <'200':
                listAnalisis.append([row[0],'MUY BAJO'])
            elif row[4] >='200' and row[4]<'300':
                listAnalisis.append([row[0],'BAJO'])
            elif row[4]>='300' and row[4] <'500':
                listAnalisis.append([row[0],'MEDIO'])
            elif row[4] >='500' and row[4] <'600':
                listAnalisis.append([row[0],'ALTO'])
            elif row[4]>='600':
                listAnalisis.append([row[0],'MUY ALTO'])
            listprecioBajo.append([float(row[3]),row[0]])
            listprecioAlto.append([float(row[2]),row[0]])
    bajo=min(listprecioBajo) 
    alto=max(listprecioAlto) 
    date_lowest=bajo[1]
    lowest_value =bajo[0]
    date_highest =alto[1]
    highest_value = alto[0] 
    
    with open('analisis_archivo.csv','w',newline='') as csvfile:
        spamwriter=csv.writer(csvfile, delimiter='\t',quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['Fecha','Concepto'])
        spamwriter.writerows(listAnalisis)

    
    return date_lowest, lowest_value, date_highest, highest_value

"""
NO COLOCAR CÓDIGO FUERA DE LAS FUNCIONES QUE USTED CREE
Esta línea de código que sigue permite saber si su solución al ejercicio es correcto
Por favor NO ELIMINARLA, NO MODIFICARLA
"""
pruebas_codigo_estudiante(solucion)