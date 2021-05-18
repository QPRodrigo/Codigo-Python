"""
Panecillos es un juego simple que puedes jugar con un amigo. Tu amigo piensa un número
aleatorio de 3 cifras diferentes, y tú intentas adivinar qué número es. Luego de cada intento, tu
amigo te dará tres tipos de pistas:
*Panecillos – Ninguna de las tres cifras del número que has conjeturado está en el número secreto.
*Pico – Una de las cifras está en el número secreto, pero no en el lugar correcto.
*Fermi – Tu intento tiene una cifra correcta en el lugar correcto.
Puedes recibir más de una pista luego de un intento. Si el número secreto es 456 y tú conjeturas
546, la pista sería "fermi pico pico". El número 6 da "Fermi" y el 5 y 4 dan "pico pico".
"""
import random

#Funcion para mostrar el texto introductorio
def textoIntroduccion(digitosNumero, numeroIntentos):
    print('\n\n')
    print('===================================================================')
    print(f'Estoy pensando en un número de {digitosNumero} dígitos. Intenta adivinar cuál es.')
    print('Aquí hay algunas pistas:')
    print('Cuando digo: \tEso significa:')
    print('Pico         \tUn dígito es correcto pero en la posición incorrecta.')
    print('Fermi        \tUn dígito es correcto y en la posición correcta.')
    print('Panecillos   \tNingún dígito es correcto.')  
    print('--------------------------------------------------------------------')
    print(f'He pensado en un número de . Tienes {numeroIntentos} intentos para adivinarlo.')
    print('--------------------------------------------------------------------')

#Funcion para obtener un numero secreto
def ObtenerNumSecreto(digitosNum):
    Lista_Digitos = '0 1 2 3 4 5 6 7 8 9'.split()
    random.shuffle(Lista_Digitos)
    numSecreto=''
    while True:
        for i in range(digitosNum):
            numSecreto = numSecreto + str(Lista_Digitos[i])
        if numSecreto[0]!='0' :
            return numSecreto

#Funcion para mostrar el resultado de la conjetura
def obtenerPistas(conjetura, numSecreto):
    if conjetura == numSecreto:
        return 'Lo has adivinado!!!'
    
    pista=[]
    for i in range(len(conjetura)):
        if conjetura[i]==numSecreto[i]:
            pista.append('Fermi')
        elif conjetura[i] in numSecreto:
            pista.append('Pico')
    if len(pista) == 0:
        return 'Panecillos'
    #Ordena de forma alfabetica
    pista.sort()
    return ' '.join(pista)

#Funcion para revisar que solo se ingresen numeros
def esSoloDigitos(num):
    if num == '':
        return False
    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False
    return True

#Funcion jugar de nuevo
def jugarDeNuevo():
    print('¿Deseas volver a jugar? (si o no)')
    return input().lower().startswith('s')

#Funcion principal
def main():
    digitosNumero = 3
    numMaximoIntentos = 10
    while True:
        #Se muestra el texto de introduccion
        textoIntroduccion(digitosNumero, numMaximoIntentos)
        #Se obtiene un numero alazar
        numSecreto = ObtenerNumSecreto(digitosNumero)
        numeroIntentos=1
        while numeroIntentos <= numMaximoIntentos:
            conjetura=''
            #Entra o repite el bucle cuando esta vacio o tiene caracteres alfanumericos en la conjetura 
            while len(conjetura) != digitosNumero or not esSoloDigitos(conjetura):
                print(f'Conjetura: {numeroIntentos}')
                conjetura = input()
                
            pista = obtenerPistas(conjetura, numSecreto)
            print(pista)
            numeroIntentos = numeroIntentos + 1

            #Si son iguales, se termina el bucle
            if conjetura == numSecreto:
                break
            #Se termino los intentos
            if numeroIntentos > numMaximoIntentos:
                print(f'Te has quedado sin intentos. La respuesta era {numSecreto}')

        if not jugarDeNuevo():
            break

if __name__=='__main__':
    main()