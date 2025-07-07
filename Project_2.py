# 1. Longitud de una frase

# Solicitar al usuario una palabra
palabra = input("Introduce una palabra: ")

# Obtener la longitud de la palabra
longitud = len(palabra)

# Verificar la longitud y dar el mensaje correspondiente
if 4 <= longitud <= 8:
    print ('La palabra es correcta')
elif longitud <= 8:
    print (f'Hacen falta letras. Solo tiene {longitud} letras.')
else:
    print (f'Sobran letras. Tiene {longitud} letras.')
    
    

# 2. Encuentra el cuadrante

# Solicitar al usuario las coordenadas X y Y
x = int(input("Introduce la coordenada X (diferente de 0): "))
y = int(input("Introduce la coordenada Y (diferente de 0): "))

# Verificar que ninguna coordenada sea 0
if x == 0 or y == 0:
    print("Error: Las coordenadas no pueden ser 0. Inténtalo de nuevo.")
else:
    # Determinar el cuadrante
    if x > 0 and y > 0:
        print("El punto se encuentra en el cuadrante I.")
    elif x < 0 and y > 0:
        print("El punto se encuentra en el cuadrante II.")
    elif x < 0 and y < 0:
        print("El punto se encuentra en el cuadrante III.")
    elif x > 0 and y < 0:
        print("El punto se encuentra en el cuadrante IV.")
