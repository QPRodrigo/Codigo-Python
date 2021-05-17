"""
En este juego, el jugador está en una tierra llena de dragones.
Todos los dragones viven en cuevas junto a sus grandes montones 
de tesoros encontrados. Algunos dragones son amigables, y 
compartirán sus tesoros contigo. Otros son codiciosos y hambrientos, 
y se comerán a cualquiera que entre a su cueva. 
El jugador se encuentra frente a dos cuevas, una con un dragón 
amigable y la otra con un dragón hambriento. El jugador tiene que
elegir entre las dos.
"""
import time
import random

def mostrarIntroduccion():
    print('.- Estas en una llena de daragones.')
    print('Frente a ti hay dos cuevas. ')
    print('En una de ellas, el dragon es generoso y amigable')
    print('y compartira su tesoro contigo.')
    print('El otro dragon es codicioso y esta hambriento,')
    print('y te devorara inmediatamente\n')

def CuevaTesoro():
    return random.randint(1,2)

def CuevaElegida():
    cueva=int(input('¿A que cueva quieres entrar? (1 ó 2)\n'))
    return cueva

def Suspenso():
    print('Te aproximas a la cueva...')
    time.sleep(2)
    print('Es oscura y espeluznante...')
    time.sleep(2)
    print('Un gran dragon aparece subitamente frente a tí!! Abre sus fauces y ...')
    time.sleep(2)

def explorarcueva(tesoro, cueva_elegida):
    if cueva_elegida == 1 or cueva_elegida ==2:
        if cueva_elegida == tesoro:
            print('Te regala su tesoro!!!')
        else:
            print('Te engulle de un bocado!!!')
    else:
        print('Debes de escoger una cueva (1 ó 2)')

def jugarDenuevo():
    juego = input('Quieres Jugar de nuevo?? (Si o No) \n')
    juego.lower()
    return juego

def main():
    jugar_Denuevo ='s'
    while jugar_Denuevo == 'si' or jugar_Denuevo == 's':
        mostrarIntroduccion()
        tesoro=CuevaTesoro()
        cueva_elegida=CuevaElegida()
        Suspenso()
        explorarcueva(tesoro, cueva_elegida)
        jugar_Denuevo=jugarDenuevo()

if __name__=='__main__':
    main()