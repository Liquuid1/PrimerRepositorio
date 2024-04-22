from random import randrange

def display_board(board): #Muestra el tablero en la consola.
    for o in range(3):
        print("+-------"*3+"+")
        print(f"|       "*3+"|")
        print(f"|   {board[o][0]}   |   {board[o][1]}   |   {board[o][2]}   |")
        print(f"|       "*3+"|")
    print("+-------"*3+"+")


def enter_move(board): #Ingresa los movimientos del usuario, tambien verifica que el movimiento sea correcto.
    print("Ingresa tu movimiento: ",end="")
    while True:
        mov = int(input())
        if mov>0 and mov<10:
            for i in range(3):
                for o in range(3):
                    if mov==board[i][o]:
                        board[i][o]="O"
                        return board
            print("Ingresa un movimiento correcto: ",end="")
        else:
            print("Ingrese una casilla valida: ",end="")


def make_list_of_free_fields(board): #Cuenta cuantos movimientos se pueden hacer.
    aux = []
    for i in range(3):
        for o in range(3):
            if board[i][o] not in ["O","X"]:
                aux.append((i,o))
    return aux
            


def victory_for(board, sign): #Señala si es que alguien ya gano el juego.
    if sign=="X":
        who="PC"
    elif sign=="O":
        who="Jugador"
    
    diagonal1 = True
    diagonal2 = True
    for i in range(3):
        if board[i][0]==sign and board[i][1]==sign and board[i][2]==sign:
            return who
        if board[0][i]==sign and board[1][i]==sign and board[2][i]==sign:
            return who
        if board[i][i]!=sign:
            diagonal1=False
        if board[i-2][i-2]!=sign:
            diagonal2=False
    if diagonal1 or diagonal2:
        return who
    return None

def draw_move(board):#Hace que la maquina juegue, no tiene ninguna IA, es solo azar.
    while True:
        x=randrange(9)
        for i in range(3):
            for o in range(3):
                if x==board[i][o]:
                    board[i][o]="X"
                    return(board)
                
def initiate_board(board): #Inicia el tablero con una X al medio.
    board = []
    row = [i+1 for i in range(3)]
    board.append(row)
    row = [i+4 for i in range(3)]
    board.append(row)
    row = [i+7 for i in range(3)]
    board.append(row)
    board[1][1]="X"
    return board

board = []
board = initiate_board(board)

free = make_list_of_free_fields(board)
display_board(board)

while len(free)!=0:
    board = enter_move(board)
    win = victory_for(board,"O")
    if win!=None:
        print("Me ganaste :(")
        break 

    draw_move(board)

    display_board(board)
    win = victory_for(board,"X")
    if win=="PC":
        print("JAJAJA TE GANE!!")
        break

    free = make_list_of_free_fields(board)

if len(free)==0:
    print("Empatamos =D")

