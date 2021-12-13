from math import sqrt
import numpy as np
#NOTA: PARA ESTE RETO PUEDES PROBAR TU PROGRAMA, DANDO CLICK EN LA NAVE ESPACIAL
#LA CONSOLA TE DARÁ INSTRUCCIONES SI PUEDES EVALUAR O NO TU CÓDIGO

#En este espacio podrás programar las funciones que deseas usar en la función solución (NO ES OBLIGATORIO CREAR OTRAS FUNCIONES)
"""Inicio espacio para programar funciones propias"""
def crearMatriz(a):
    n = 1
    o = 2
    u = 1
    while u != a:
        n = n + 1
        u = u + o
        o = o + 1
    return n


#PUEDES PROGRAMAR CUANTAS FUNCIONES DESEES 

"""Fin espacio para programar funciones propias"""

def solucion(a):
    """
    En esta función deberás programar tu solución.
    Explicación del parámetro que recibe:
    - a: Es un vector unidimensionalde numpy, (No te preocupes si NO conoces numpy,
        el manejo que debes darle es IGUAL al de una lista de Python)
        El largo de la lista lo puedes calcular así: L = len(a)
        Para indexar el elemento en la posición i se hace así (Igual como una lista):
            a[i] 
            
    Explicación de lo que debe retornar:
    -matriz: Puede ser de dos tipos (COMO TE SIENTAS MÁS CÓMODO)
        Una matriz de numpy O una lista de listas (El calificador está en las condiciones
        para recibit cualquiera de los dos tipos), en esta matriz debes guardar los
        elementos que hay en el vector a como se especifica en el enunciado
    """
    L = len(a)
    n = crearMatriz(L)
    matriz = np.zeros((n,n))
    acu = 0
    for i in range(matriz.shape[0]):
        for j in range(matriz.shape[1]):
            if i >= j:
                for k in range(acu,acu + 1):
                    matriz[i,j] = a[k]
                acu = acu + 1
    
    return matriz
    
"""
Estas líneas de código que siguen, permiten probar si su ejercicio es correcto
"""
#NO MODIFICAR
l = [8, 60, 72, 35, 26, 75, 15, 12, 33, 54]
matriz_correcta = np.array([[ 8.,  0.,  0.,  0.], [60., 72.,  0.,  0.], [35., 26., 75.,  0.], [15., 12., 33., 54.]])
matriz_estudiante = np.array(solucion(l))
print("LISTA ENTREGADA:\n", l,"\n")
print("===SALIDA ESPERADA===\nMatriz:\n", matriz_correcta,"\n")
print("===TU SALIDA===\nMatriz:\n", matriz_estudiante,"\n")

for i in range(matriz_correcta.shape[0]):
    for j in range(matriz_correcta.shape[1]):
        if matriz_correcta[i,j] != matriz_estudiante[i,j]:
            print("Las salidas no coinciden, ¡Estás olvidando algo en tu código!")
            exit()
print("Todo se ve correcto, ¡Procede a calificar tu código!")