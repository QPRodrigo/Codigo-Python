"""
En este juego, colocamos coloca dispositivos de sonar en varios lugares en el océano para
localizar cofres de tesoros hundidos. El sonar es una tecnología que utilizan los barcos 
para localizar objetos debajo del mar. Los dispositivos de sonar (en este juego) le dirán 
al jugador que tan lejos están del tesoro más cercano, pero no en qué dirección. Pero al 
colocar diversos sonares, el jugador puede deducir donde se encuentra el tesoro.
Hay tres cofres a recuperar, pero el jugador sólo tiene dieciséis dispositivos de sonar 
para encontrarlos. Imagina que no puedes ver el cofre de tosoro en la siguiente imágen. 
Debido a que cada sonar puede sólo encontrar distancia, no dirección, los posibles 
lugares en que podría encontrarse el tesoro corresponden a un cuadrado alrededor del 
dispositivo.

Pero múltiples dispositivos de sonar trabajando en conjunto pueden reducir el área a un punto
exacto donde las áreas se intersecten.
"""
import random
import sys
def mostrarIntrucciones():
    print('''
Instrucciones: 
    Eres el capitán de Simón, un buque cazador de tesoros. Tu misión actual
    es encontrar los tres cofres con tesoros perdidos que se hallan ocultos 
    en la parte del océano en que te encuentras y recogerlos.
    Para jugar, ingresa las coordenadas del punto del océano en que quieres
    colocar un dispositivo sonar. El sonar puede detectar cuál es la distancia
    al cofre más cercano.
    Por ejemplo, la "d" abajo indica dónde se ha colocado el dispositivo, y 
    los números 2 representan los sitios a una distancia 2 del dispositivo. 
    Los números 4 representan los sitios a una distancia 4 del dispositivo.

                            444444444
                            4       4
                            4 22222 4
                            4 2   2 4
                            4 2 d 2 4
                            4 2   2 4
                            4 22222 4
                            4       4
                            444444444

    Pulsa enter para continuar...''')
    input()
    print('''
    Por ejemplo, aquí hay un cofre del tesoro (la c) ubicado a
    una distancia 2 del dispositivo sonar (la d):

                                22222
                                c   2
                                2 d 2
                                2   2
                                22222
    
    El punto donde el dispositivo fue colocado se indicará con una d.

    Los cofres del tesoro no se mueven. Los dispositivos sonar pueden detectar
    cofres hasta una distancia 9. Si todos los cofres están fuera del alcance,
    el punto se indicará con un O.

    Si un dispositivo es colocado directamente sobre un cofre del tesoro, has
    descubierto la ubicación del cofre, y este será recogido. El dispositivo
    sonar permanecerá allí.

    Cuando recojas un cofre, todos los dispositivos sonar se actualizarán para
    localizar el próximo cofre hundido más cercano.
    Pulsa enter para continuar...\n''')
    input('\n')

def obtenerNuevoTablero():
    # Crear una nueva estructura de datos para un tablero de 60x15.
    tablero = []
    # la lista principal es una lista de 60 listas
    for x in range(60):
        tablero.append([])
        # cada lista en la lista principal tiene 15 cadenas de un solo caracter
        for y in range(15): 
            #Usar diferentes caracteres para el océano para hacerlo más fácil de leer.
            if random.randint(0,1) == 0:
                tablero[x].append('~')
            else:
                tablero[x].append('-')
    return tablero

# Crear una lista de estructuras de datos cofre (listas de dos ítems con coordenadas x, y)
def obtenerCofresAleatorios(numCofres):
    cofres =[]
    for i in range(numCofres):
        cofres.append([random.randint(0,59),random.randint(0,14)])
    return cofres

#Dibuja la estructura de datos del tablero.
def dibujarTablero(tablero):
    lineah = ' ' # espacio inicial para los números a lo largo del lado izquierdo del tablero
    for i in range(0,6):
        lineah = lineah + (' ' * 9) + str(i)

    #imprimir los numeros a lo largo del borde superior
    print(lineah)
    print('    ' + ('0123456789')*6)
    print()

    #imprimir cada una de las 15 filas
    for i in range(15):
        #los numeros de una sola cifra deben ser precedidos por un espacio extra
        if i < 10:
            espacioExtra='  '
        else:
            espacioExtra=' '
        #Se imprime cada linea que le corresponde al tablero llamando a la funcion
        print(f'{espacioExtra}{i} {obtenerFila(tablero, i)} {i}') 
    
    #imprimir los numeros a lo largo del borde inferior
    print()
    print('    '+('0123456789'*6))
    print(lineah)

## Devuelve una cadena con la estructura de datos de un tablero para una fila determinada.
def obtenerFila(tablero, fila):
    filaTablero = ''
    for i in range(60):
        filaTablero = filaTablero + tablero[i][fila]
    return filaTablero

#Se ingresar los valores del movimiento del jugador
def ingresarMovidaJugador():
    print('¿Donde quieres dejar caer el siguiente dispositivo sonar? (0-59)(o teclea salir)')
    while True:
        movida = input()
        if movida.lower() == 'salir':
            print('Gracias por jugar!!')
            sys.exit()#Se finaliza la ejecucion
        #La entrada se convierte en una cadena
        movida = movida.split()
        #se valida si los datos son correctos
        if len(movida) == 2 and movida[0].isdigit() and movida[1].isdigit() and esMovidaValida(int(movida[0]), int(movida[1])):
            return [int(movida[0]), int(movida[1])]
        print('Ingresa un numero de 0 a 59, un espacio, y luego un numero de 0 a 14. ')

# Devuelve True si las coordenadas pertenecen al tablero, de lo contrario False.
def esMovidaValida(x, y):
    return x>= 0 and x<= 59 and y >= 0  and y <= 14

# Cambia la estructura de datos del tablero agregando un caracter de dispositivo sonar. 
# Elimina los cofres de la lista de cofres a medida que son encontrados. Devuelve False si la movida no es válida.
# En caso contrario, devuelve una cadena con el resultado de esa movida.
def realizarMovida(tablero, cofres, x, y):
    #Si no es valida retorna un false
    if not esMovidaValida(x, y):
        return False

    #La mayor distancia de un punto a otro es 100
    menorDistancia = 100 

    #las coordenas de los cofres, va comparando y reemplanzando
    for cx, cy in cofres:
        #abs valor absoluto
        if abs(cx - x) > abs(cy - y):
            distancia = abs(cx - x)
        else:
            distancia = abs(cy - y )

        # queremos el cofre más cercano. La menor distancia es reemplazada
        if distancia < menorDistancia:
            menorDistancia = distancia      

    #Si encuentra un cofre      
    if menorDistancia == 0:
        # ¡xy está directamente sobre un cofre!
        cofres.remove([x, y])
        return 'Has encontrado un cofre del tesoro hundido!!'
    #Si no encuentra un cofre
    else:
        #Si esta cerca de un cofre
        if menorDistancia < 10:
            tablero[x][y]=str(menorDistancia)
            return f'Tesoro detectado a una distancia {menorDistancia} del dispositivo sonar'
        #Si esta lejos de un cofre
        else:
            tablero[x][y]='X'
            return 'El sonar no ha detectado nada. Todos los cofres estan fuera del alcance del dispositivo. '

#Funcion de jugar de nuevo
def jugarDeNuevo():
    print('¿Desea jugar de nuevo? (Si o No)')
    return input().lower().startswith('s')

def main():
    #Numero de Cofres
    numero_cofres=3
    #titulo
    print('\n\t\tS O N A R !!!!\n')
    print('¿Te gustaria ver las instrucciones ? (si/no)')
    #Muestra las Instrucciones si se desea
    if input().lower().startswith('s'):
        mostrarIntrucciones()
    #Bucle infinito
    while True:
        #Numero de intentos
        dispositivosSonar = 16
        #Se obtiene el tablero en una matriz
        elTablero = obtenerNuevoTablero()
        #Se obtiene la hubicacion de los cofres aleatorios
        losCofres = obtenerCofresAleatorios(numero_cofres)
        #Se muestra el tablero
        dibujarTablero(elTablero)
        #Se registra los movimientos previos
        movidasPrevias=[]
        #Bucle si el numero de dispositivos es mayor
        while dispositivosSonar > 0:
            #Comienzo de un turno

            #Mostrar el estado de los dispositivos sonar / cofres
            #Si hay mas de un dispositivo se agrega la 's'(dispositivos)
            if dispositivosSonar > 1: 
                extraSsonar = 's'
            else:
                extraSsonar = ''
            #Si hay mas de un cofre se agrega la 's'(cofres)
            if len(losCofres) > 1:
                extraScofre = 's'
            else: 
                extraScofre = ''
            print(f'Aun tienes {dispositivosSonar} dispositivo{extraSsonar} sonar.Falta encontrar {len(losCofres)} cofre{extraScofre}')
            
            #Se retorno valores de la funcion
            x,y = ingresarMovidaJugador()

            #debemos registrar todas las movidas para que los dispositivos sonar puedan ser actualizados.
            movidasPrevias.append([x,y])

            #Se ingresa en tablero los datos ingresados
            resultadoMovida = realizarMovida(elTablero, losCofres, x ,y)
            if resultadoMovida ==False:
                continue
            else:
                if resultadoMovida == 'Has encontrado un cofre del tesoro hundido!!':
                    #actualizar todos los dispositivos sonar presentes en el mapa, cuando se detecta uno
                    for x, y in movidasPrevias:
                        realizarMovida(elTablero, losCofres, x, y)
                #Dibuja el tablero
                dibujarTablero(elTablero)
                print(resultadoMovida)

            #Cuando se encuentra todos los cofres
            if len(losCofres) == 0:
                print('Has encontrado todos los cofres del tesoro! !Felictaciones y buena partida!!')
                break
            dispositivosSonar = dispositivosSonar - 1
        
        #Cuando no hay dispostivos de sonar o intentos
        if dispositivosSonar == 0:
            print('Nos hemos quedado sin dispositivos sonar!! Ahora tenemos que dar la vuelta y dirigirnos!!!')
            print('de regreso a casa dejando tesoros en el mar!!! Juego terminado.')
            print('\t\tLos cofres restantes estaban aqui:')
            #Imprime la ubicacion de cada cofre
            for x,y in losCofres:
                print(f'\t\t{x}{y}')

        #Consulta al jugador si desea jugar de nuevo
        if not jugarDeNuevo():
            sys.exit()

if __name__=='__main__':
    main()