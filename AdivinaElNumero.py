"""
La computadora pensará un número aleatorio entre 1 y 20, 
y te pedirá que intentes adivinarlo. La computadora te 
dirá si cada intento es muy alto o muy bajo. Tú ganas si 
adivinas el número en seis intentos o menos.
"""
#Importar la libreria random
import random
#Asignar un valor a un dato
nombre = input('Hola! ¿Como te llamas?\n')
print(f'Bueno, {nombre}, estoy pensando en un numero entre 1 y 20')
#Asignar un numero randon a una variable
numero_randon = random.randint(1,20)
#Variable de intentos
intentos_Realizados = 6
#Bucle de los 6 intentos
while intentos_Realizados <= 6 and intentos_Realizados >0:
    #Asignar el valor a una variable 
    estimación = int(input(f'Intenta Adivinar en {intentos_Realizados} intentos\n'))
    #Si es menor la estimacion
    if estimación < numero_randon:
        print('Tu estimación es muy baja.')
    #Si es mayor la estimacion  
    elif estimación > numero_randon:
        print('Tu estimación es muy alta')
    #Si es igual la estimacion
    else:
        break
    #Reducir el numero de intentos
    intentos_Realizados=intentos_Realizados-1

#Resultado si encuentra el resultado  
if(estimación == numero_randon):
    print(f'Buen Trabajo!!! {nombre} ¡Has adivinado mi número en {numero_randon} en {intentos_Realizados} intentos!')
#Resultado si no encuentra el resultado  
else:
    print(f'Pues no!!! {nombre} ¡El número que estaba pensando era {numero_randon}!!')
