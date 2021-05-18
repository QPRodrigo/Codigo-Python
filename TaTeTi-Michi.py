"""
Dos personas pueden jugar Ta Te Ti/Michi con lápiz y papel.
Un jugador es X y el otro es O. En un tablero consistente 
en nueve cuadrados, los jugadores toman turnos para colocar 
sus X u O. Si un jugador consigue ubicar tres de sus marcas
en el tablero sobre la misma línea, columna o alguna de las 
dos diagonales, gana. Cuando el tablero se llena y ningún 
jugador ha ganado, el juego termina en empate.
"""

# Ta Te Ti
import random
def dibujarTablero(tablero):
    # Esta función dibuja el tablero recibido como argumento.
    # "tablero" es una lista de 10 cadenas representando la pizarra (ignora índice 0)
    print('   |   |')
    print(' ' + tablero[7] + ' | ' + tablero[8] + ' | ' + tablero[9])
    print('   |   |')
    print('------------')
    print('   |   |')
    print(' ' + tablero[4] + ' | ' + tablero[5] + ' | ' + tablero[6])
    print('   |   |')
    print('------------')
    print('   |   |')
    print(' ' + tablero[1] + ' | ' + tablero[2] + ' | ' + tablero[3])
    print('   |   |')


# Permite al jugador typear que letra desea ser.
# Devuelve una lista con las letras de los jugadores como primer item, y la de la computadora como segundo.
def ingresaLetraJugador():
    letra = '' #Inicializa la variable
    while not (letra == 'X' or letra == 'O'):
        print('¿Deseas ser X o O?')
        letra = input().upper()
    if letra == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def quienComienza():
    # Elije al azar que jugador comienza.
    if random.randint(0, 1) == 0:
        return 'La computadora'
    else:
        return 'El jugador'

def jugarDeNuevo():
    # Esta funcion devuelve True (Verdadero) si el jugador desea volver a jugar, de lo contrario devuelve False (Falso).
    print('¿Deseas volver a jugar? (sí/no)?')
    return input().lower().startswith('s')

#se guarda la letra del jugador(X ó O) en la posicion escogida lista: 
def hacerJugada(tablero, letra, jugada):
    tablero[jugada] = letra

def esGanador(ta, le):
    # Dado un tablero y la letra de un jugador, devuelve True (verdadero) si el mismo ha ganado.
    # Utilizamos reemplazamos tablero por ta y letra por le para no escribir tanto.
    return ((ta[7] == le and ta[8] == le and ta[9] == le) or # horizontal superior
    (ta[4] == le and ta[5] == le and ta[6] == le) or # horizontal medio
    (ta[1] == le and ta[2] == le and ta[3] == le) or # horizontal inferior
    (ta[7] == le and ta[4] == le and ta[1] == le) or # vertical izquierda
    (ta[8] == le and ta[5] == le and ta[2] == le) or # vertical medio
    (ta[9] == le and ta[6] == le and ta[3] == le) or # vertical derecha
    (ta[7] == le and ta[5] == le and ta[3] == le) or # diagonal
    (ta[9] == le and ta[5] == le and ta[1] == le)) # diagonal

def obtenerDuplicadoTablero(tablero):
    # Duplica la lista del tablero y devuelve el duplicado.
    dupTablero = []
    for i in tablero:
        dupTablero.append(i)
    return dupTablero

# Devuelte true si hay espacio para efectuar la jugada en el tablero.
def hayEspacioLibre(tablero, jugada):
    return tablero[jugada] == ' '

def obtenerJugadaJugador(tablero):
    # Permite al jugador escribir su jugada.
    jugada = ' '
    #Repite si la asignacion de jugada es diferente a un numero - ó - Si ya ocupa un espacio 
    while jugada not in '1 2 3 4 5 6 7 8 9'.split() or not hayEspacioLibre(tablero, int(jugada)):
        print('¿Cuál es tu próxima jugada? (1-9)')
        jugada = input()
    return int(jugada)

def elegirAzarDeLista(tablero, listaJugada):
    # Devuelve una jugada válida en el tablero de la lista recibida.
    # Devuelve None si no hay ninguna jugada válida.
    jugadasPosibles = []
    for i in listaJugada:
        if hayEspacioLibre(tablero, int(i)):
            jugadasPosibles.append(i)
    if len(jugadasPosibles) != 0:
        return random.choice(jugadasPosibles)
    else:
        return None
"""
El algoritmo de la IA consiste en los siguientes pasos:
    1. Primero, ver si hay un movimiento con el que la computadora pueda ganar el juego. Si lo
    hay, hacer ese movimiento. En caso contrario, ir al paso 2.
    2. Ver si existe un movimiento disponible para el jugador que pueda hacer que la
    computadora pierda el juego. Si existe, la computadora debería jugar en ese lugar para
    bloquear la jugada ganadora. En caso contrario, ir al paso 3.
    3. Comprobar si alguna de las esquinas (espacios 1, 3, 7, ó 9) está disponible. Si lo está,
    mover allí. Si no hay ninguna esquina disponible, ir al paso 4.
    4. Comprobar si el centro está libre. Si lo está, jugar en el centro. Si no lo está, ir al paso 5.
    5. Jugar en cualquiera de los lados (espacios 2, 4, 6, u 8). No hay más pasos, ya que si
    hemos llegado al paso 5 los únicos espacios restantes son los lados.
"""
def obtenerJugadaComputadora(tablero, letraComputadora):
    # Dado un tablero y la letra de la computadora, determina que jugada efectuar.
    if letraComputadora == 'X':
        letraJugador = 'O'
    else:
        letraJugador = 'X'

    # Aquí está nuestro algoritmo para nuestra IA (Inteligencia Artifical) del Ta Te Ti.
    # Primero, verifica si podemos ganar en la próxima jugada
    for i in range(1, 10):
        copia = obtenerDuplicadoTablero(tablero)
        if hayEspacioLibre(copia, i):
            hacerJugada(copia, letraComputadora, i)
            if esGanador(copia, letraComputadora):
                return i

    # Verifica si el jugador podría ganar en su próxima jugada, y lo bloquea.
    for i in range(1, 10):
        copia = obtenerDuplicadoTablero(tablero)
        if hayEspacioLibre(copia, i):
            hacerJugada(copia, letraJugador, i)
            if esGanador(copia, letraJugador):
                return i

    # Intenta ocupar una de las esquinas de estar libre.
    jugada = elegirAzarDeLista(tablero, [1, 3, 7, 9])
    if jugada != None:
        return jugada

    # De estar libre, intenta ocupar el centro.
    if hayEspacioLibre(tablero, 5):
        return 5

    # Ocupa alguno de los lados.
    return elegirAzarDeLista(tablero, [2, 4, 6, 8])

def tableroCompleto(tablero):
    # Devuelve True si cada espacio del tablero fue ocupado, caso contrario devuele False.
    for i in range(1, 10):
        if hayEspacioLibre(tablero, i):
            return False
    return True

def main():
    print('¡Bienvenido al Ta - Te - Ti!')
    while True:
        # Resetea el tablero
        elTablero = [' '] * 10
        letraJugador, letraComputadora = ingresaLetraJugador()
        turno = quienComienza()
        print(turno + ' irá primero.')
        juegoEnCurso = True

        while juegoEnCurso:
            # Turno del jugador
            if turno == 'El jugador':
                dibujarTablero(elTablero)
                jugada = obtenerJugadaJugador(elTablero)
                hacerJugada(elTablero, letraJugador, jugada)

                if esGanador(elTablero, letraJugador):
                    dibujarTablero(elTablero)
                    print('¡Felicidades, has ganado!')
                    juegoEnCurso = False
                else:
                    if tableroCompleto(elTablero):
                        dibujarTablero(elTablero)
                        print('¡Es un empate!')
                        break
                    else:
                        turno = 'La computadora'
            # Turno de la computadora
            else:
                jugada = obtenerJugadaComputadora(elTablero, letraComputadora)
                hacerJugada(elTablero, letraComputadora, jugada)
                if esGanador(elTablero, letraComputadora):
                    dibujarTablero(elTablero)
                    print('¡La computadora te ha vencido! Has perdido.')
                    juegoEnCurso = False
                else:
                    if tableroCompleto(elTablero):
                        dibujarTablero(elTablero)
                        print('¡Es un empate!')
                        break
                    else:
                        turno = 'El jugador'
        if not jugarDeNuevo():
            break

if __name__=='__main__':
    main()