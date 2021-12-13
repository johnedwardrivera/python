#NO ELIMINAR LA SIGUIENTE IMPORTACIÓN, sirve para probar tu código en consola
from pruebas import pruebas_codigo_estudiante
"""NOTAS: 
    -PARA ESTE RETO PUEDES PROBAR TU PROGRAMA, DANDO CLICK EN LA NAVE ESPACIAL
    -LA CONSOLA TE DARÁ INSTRUCCIONES SI PUEDES EVALUAR O NO TU CÓDIGO
"""


"""Inicio espacio para programar funciones propias"""
#En este espacio podrás programar las funciones que deseas usar en la función solución (ES OPCIONAL




"""Fin espacio para programar funciones propias"""

def actualizar_estado_pestana(operaciones_usuario, pagina_default):
    #ESTA ES LA FUNCIÓN A LA QUE LE DEBES GARANTIZAR LOS RETORNOS REQUERIDOS EN EL ENUNCIADO.
    pagina_actual = pagina_default 
    pila_atras=[]
    pila_adelante=[]
    for i in range(len(operaciones_usuario)):
        if operaciones_usuario[i]!="atras" and operaciones_usuario[i] != "adelante":
            if operaciones_usuario[i] == pagina_actual:
                pass
            else:
                pila_atras.append(pagina_actual)
                pagina_actual = operaciones_usuario[i]
                if len(pila_adelante) > 0:
                    for j in range(len(pila_adelante)):
                        pila_adelante.pop()
        elif operaciones_usuario[i] =="atras":
            pila_adelante.append(pagina_actual) 
            pagina_actual = pila_atras[-1]
            pila_atras.pop() 
        elif operaciones_usuario[i]== "adelante":
            pila_atras.append(pagina_actual) 
            pagina_actual=pila_adelante[-1]
            pila_adelante.pop()
    return pila_atras, pagina_actual, pila_adelante

"""
NO PEDIR DATOS CON LA FUNCIÓN input(), NO COLOCAR CÓDIGO FUERA DE LAS FUNCIONES QUE USTED CREE
Esta línea de código que sigue, permite probar si su ejercicio es correcto
Por favor NO ELIMINARLA
"""
pruebas_codigo_estudiante(actualizar_estado_pestana)