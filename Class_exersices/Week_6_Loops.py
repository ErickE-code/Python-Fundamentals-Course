

jugador1 = input('Introduce tu edad')
edad = 0
while edad != jugador1:
    edad = input('Jugador 2 adivina la edad')
    if edad<jugador1:
        print ('te faltan años')
    else:
        print ('Te pasaste de años')
print ('Lograste adivinar la edad. Felicidades')
