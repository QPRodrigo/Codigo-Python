"""
El Cifrado César fue uno de los primeros sistemas de cifrado que se inventaron. Con este cifrado,
para encriptar un mensaje se toma cada letra del mismo (en criptografía, estas letras se llaman
símbolos porque pueden ser letras, números o cualquier otro signo) y se la reemplaza con una
letra "desplazada". Si desplazas la letra A un espacio, obtienes la letra B. Si desplazas la A dos
espacios, obtienes la letra C.
"""

#Variable Global
TAMANIO_MAX_CLAVE = 26

#Metodo para obtener si es encriptar o desencriptar
def obtenerModo():
    while True:
        print('¿Deseas encriptar o desencriptar y/o brutar un mensaje?')
        modo = input().lower()
        if modo in 'encriptar e desencriptar d bruta b'.split():
            return modo
        else:
            print('Ingresa "encriptar" o  "e" o "desencriptar" o "d" o "bruta" o "b" ')

#Obtener el mensaje
def obtenerMensaje():
    print('Ingresa tu mensaje: ')
    return input()

#Obtener el numero de la clave
def obtenerClave():
    clave = 0
    while True:
        print(f'Ingresa el numero de clave (1-{TAMANIO_MAX_CLAVE})')
        clave = int(input())
        if (clave>=1 and clave <= TAMANIO_MAX_CLAVE):
            return clave 

#Obtener el mensaje traducido
def obtenerMensajeTraducido(modo, mensaje, clave):
    #Desencriptar
    if modo[0] =='d':
        clave = -clave
    traduccion = ''
    for simbolo in mensaje:
        #si hay un alfanuerico
        if simbolo.isalpha():
            num = ord(simbolo)
            num +=clave
            #Si hay letras
            if simbolo.isupper():
                if num>ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num +=26
            elif simbolo.islower():
                if num > ord('z'):
                    num -=26
                elif num<ord('a'):
                    num+=26
            #Pone en una cadena los caracteres, que van cambiando
            traduccion += chr(num)
        #Si no hay alfanumerico
        else:
            traduccion += simbolo
    return traduccion

#Funcion principal
def main():
    modo = obtenerModo()
    mensaje=obtenerMensaje()
    #Cuando es diferente a b, llama una clave
    if modo[0] != 'b':
        clave = obtenerClave()
    #Imprime mensaje
    print('Tu texto traducido es: ')
    #Cuando es diferente a b
    if modo[0] != 'b':
        print(obtenerMensajeTraducido(modo, mensaje, clave))
    #Cuando es igual a b
    else:
        #Imprime todas las claves
        for clave in range(1, TAMANIO_MAX_CLAVE +1):
            print(clave, obtenerMensajeTraducido('desencriptar', mensaje, clave))


if __name__=='__main__':
    main()