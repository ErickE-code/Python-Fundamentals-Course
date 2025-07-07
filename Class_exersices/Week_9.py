

def promedio(nombre, call1, call2):
    """
    Funcion que calcula el promedio del alumno.
    """
    promedio = (call1 + call2) / 2  
    return promedio


def ingresa(numero=1):
    """
    Funcion que ingresa los datos del alumno.
    """
    lista = []
    for i in range(numero):
        nombre = input('Nombre: ')
        call1 = int(input('Calificacion 1: '))  
        call2 = int(input('Calificacion 2: '))  
        lista.append([nombre, call1, call2])
        print(nombre, promedio(nombre, call1, call2))  


numero_alumnos = int(input('Ingrese el numero de alumnos: '))
ingresa(numero_alumnos)
