tablero = ["_","_","_","_","_","_","_","_","_"]
tablero
ganador = None

#Imprimir tablero
def muestraTablero():
    print("\n")
    print('|'+ tablero[0] + "|" + tablero[1] + "|" + tablero[2] + '|'+ '              Posiciones '+'|1|2|3|')
    print('|'+ tablero[3] + "|" + tablero[4] + "|" + tablero[5] + '|'+ '                         '+'|4|5|6|')
    print('|'+ tablero[6] + '|' + tablero[7] + '|' + tablero[8] + '|'+ '                         '+'|7|8|9|')
    print("\n")
print(muestraTablero())

#Seleccion de usuario
def seleccionaJugador():
    usuario1=(input("Usuario 1 seleccione 'X' o 'O':"))
    usuario2=1
    if usuario1=='X':
        usuario2='O'
        print("Para el usuario 1:", usuario1,'Para el usuario 2: ', usuario2) 
        print("Empiezan las X")
        return usuario1,usuario2    
    if usuario1=='O':
        usuario1='O'
        usuario2='X'
        print("Para el usuario 1:", usuario1,'Para el usuario 2: ', usuario2)
        print("Empiezan las X")
        return usuario1,usuario2

#Funcion para cada Jugada
def jugada(valor):
    anoto=False
    while anoto==False: 
        posicion=int(input("Seleccione la posición a marcar (1-9): "))
        posicion -= 1
        if tablero[posicion]=="_":
            anoto=True
        else: 
            print('Posición ocupada, vuelva a intentar ')
    tablero[posicion]=valor
    print(muestraTablero())

#Funcion que verifica una triple 
def verificaGanador():
    global ganador
    lineaH()
    lineaV()
    tresEnX()

#Triple en horizontal
def lineaH():
    global ganador
    if tablero[0]==tablero[1]==tablero[2]:
        ganador=tablero[0]
    elif tablero[3]==tablero[4]==tablero[5]: 
        ganador=tablero[3]
    elif tablero[6]==tablero[7]==tablero[8]:
         ganador=tablero[6]

#Triple en vertical
def lineaV():
    global ganador
    if tablero[0]==tablero[3]==tablero[6]:
        ganador=tablero[0]
    elif tablero[1]==tablero[4]==tablero[7]: 
        ganador=tablero[1]
    elif tablero[2]==tablero[5]==tablero[8]:
         ganador=tablero[2]

#Triple en diagonal
def tresEnX():
    global ganador
    if tablero[0]==tablero[4]==tablero[8]:
        ganador=tablero[0]
    elif tablero[2]==tablero[4]==tablero[6]:
        ganador=tablero[2]

#Funcion principal del juego
def jugar():
    global ganador
    seleccionaJugador()
    print("Empieza el juego")
    print(muestraTablero())
    for i in range (5):
        print("Turno para las X")
        valor='X'
        jugada(valor)
        verificaGanador()
        if ganador != 'X' and i<4:
            for j in range (3):
                print('Turno para las O')
                valor='O'
                jugada(valor)
                verificaGanador()
                if ganador == 'O':
                    print("¡Felicidades jugador con las O! ¡¡¡¡Haz GANADO!!!!")
                    resetPlay() 
                break
        elif ganador == 'X':
            print("¡Felicidades jugador con las X! ¡¡¡¡Haz GANADO!!!!")
            resetPlay()
            break
        else:
            print("Se ha empatado el juego, ningun ganador")
            resetPlay()

#Limpiar el tablero una vez terminado el juego            
def resetPlay():
    tablero[0]='_'        
    tablero[1]='_' 
    tablero[2]='_' 
    tablero[3]='_' 
    tablero[4]='_' 
    tablero[5]='_' 
    tablero[6]='_' 
    tablero[7]='_' 
    tablero[8]='_' 

jugar()

"""Firma: Juan C. Londoño"""