
print('**********************************************************************************************')
print('                              Sistema de Validaciones Python Utel                             ')
print('**********************************************************************************************')

edad = input("Hola, ingresa tu edad: ")

if edad.isnumeric():
    pass
else:
    print("Valor ingresado no valido, por favor corrija su respuesta")
    exit()

edad = int(edad)    
    
if edad > 150:
    print("Woow, cuanto has vivido!!!")
elif edad <18:
    print("Eres demasiado joven para este curso.") 
elif edad <=0:
    print("No puedes tener 0 años ni edad negativa")
else:
    print("Felicidades, estas en los rangos de edad adecuados. Toma tu premio!!!")