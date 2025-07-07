print("""##########################################################
######### Software Registrador #########################
######################################################""")
lista = []
alumnos = 0
contador = 0
while alumnos<5:
    opcion = input ('Agregar alumno (1); Cerrar sesion (2); Repetir Menú (3)')
    if opcion =='1':
        nombre = input ('Ingrese nombre')
        lista.append (nombre)
    elif opcion =='2':
        break
    elif opcion =='3':
        continue
    else:
        contador +=1
        if contador ==4:
            print('Fallaste demasiado')
            exit ()
        print ('Volver a intentar')
print (lista)