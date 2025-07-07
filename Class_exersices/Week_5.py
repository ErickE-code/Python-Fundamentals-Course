# Solicitar al usuario el año actual
año_actual = int(input("Introduce el año actual: "))

# Solicitar otro año para calcular
año_ingresado = int(input("Introduce otro año para calcular: "))

# Comparar los años
if año_actual == año_ingresado:
    print("Has introducido el mismo año que el actual.")
elif año_ingresado < año_actual:
    diferencia = año_actual - año_ingresado
    if diferencia == 1:
        print(f"Desde el año {año_ingresado} ha pasado {diferencia} año.")
    else:
        print(f"Han pasado {diferencia} años desde el año que has introducido.")
else:
    diferencia = año_ingresado - año_actual
    if diferencia == 1:
        print(f"Para llegar a {año_ingresado} hace falta {diferencia} año.")
    else:
        print(f"Faltan {diferencia} años para llegar al año que has introducido.")