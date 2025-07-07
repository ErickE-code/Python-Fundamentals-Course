print('**********************************************************************************************')
print('                              Sistema de registro de datos Python Utel                        ')
print('**********************************************************************************************')

while True:

    name = input('Ingrese su nombre completo: ')
    edad = input("Ingrese su edad: ")
    email = input ('Ingerese su email: ')
    tel = input('Ingrese su telefono: ')

    print('\n Registro de '+name+' de edad '+edad+' ha sido guardado exitosamente.')

    with open('registro.txt','a') as archivo:
        archivo.write('Nombre: {}'.format(name))
        archivo.write(f',Edad: {edad}') 
        archivo.write(f',Email: {email}')
        archivo.write(f',Tel: {tel}') 

    opc = input('Quieres agregar otro regustro? y/n')
    
    if opc=='n':
        break
    

    print('**********************************************************************************************')