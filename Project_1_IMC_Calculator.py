print('**********************************************************************************************')
print('                             Calculadora de Índice de Masa Corporal (IMC)                     ')
print('**********************************************************************************************')

nombre = input('Ingrese su nombre: ')
apellido_paterno = input('Ingrese su apellido paterno: ')
apellido_materno = input('Ingrese su apellido materno: ')

try:
    edad = int(input("Ingrese su edad: "))
    peso = float(input("Ingrese su peso en kg: "))
    estatura = float(input("Ingrese su estatura en metros: "))
except ValueError:
    print("Por favor, ingrese valores numéricos para la edad, peso y estatura.")
else:
    imc = peso / (estatura ** 2)

    print('\nDatos ingresados:')
    print(f'Nombre completo: {nombre} {apellido_paterno} {apellido_materno}')
    print(f'Edad: {edad} años')
    print(f'Peso: {peso} kg')
    print(f'Estatura: {estatura} m')
    print(f'Índice de Masa Corporal (IMC): {imc:.2f}')

print('**********************************************************************************************')
