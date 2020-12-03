def display_board(board):
#
# Funkcja, która przyjmuje jeden parametr zawierający bieżący stan tablicy
# i wyświetla go w oknie konsoli.
    print ("+-------+-------+-------+")
    print ("|       |       |       |")
    print ("|  ",board[0][0],"  |  ",board[0][1],"  |  ",board[0][2],"  |")
    print ("|       |       |       |")
    print ("+-------+-------+-------+")
    print ("|       |       |       |")
    print ("|  ",board[1][0],"  |  ",board[1][1],"  |  ",board[1][2],"  |")
    print ("|       |       |       |")
    print ("+-------+-------+-------+")
    print ("|       |       |       |")
    print ("|  ",board[2][0],"  |  ",board[2][1],"  |  ",board[2][2],"  |")
    print ("|       |       |       |")
    print ("+-------+-------+-------+")
#

def enter_move(board):
#
    move=0
    #print("dziala!")
    accept=False
    while not accept:
        move=int(input("Jaki bedzie Twoj ruch?\n"))
        if move > 0 and move < 10:
            for i in range(3):
                if move in board[i]:
                   accept=True
        if accept==True:
            for i in range(3):
                if move in board[i]:
                    board[i][(move%3)-1] = 'O'
        else:
            print("Podaj wolne pole!")
# Funkcja, która przyjmuje parametr odzwierciedlający biężący stan tablicy,
# prosi użytkownika o wykonanie ruchu, 
# sprawdza dane wejściowe i aktualizuje tablicę zgodnie z decyzją użytkownika.
#

def make_list_of_free_fields(board):
#
    free_fields=[]
    for i in range (3):
        for j in range(3):
            if(str(board[i][j]) != 'O' and str(board[i][j]) != 'X'):
                free_fields.append( (i,j) )
    return free_fields
            
# Funkcja, która przegląda tablicę i tworzy listę wszystkich wolnych pól; 
# lista składa się z krotek, a każda krotka zawiera parę liczb odzwierciedlających rząd i kolumnę.
#

def victory_for(board, sign):
#
    if( len(make_list_of_free_fields(board)) < 5 ):
        for i in range(3):
            CounterRow=0
            counterColumn=0
            counterDiagonally=0
            k=0
            for j in range(3):
                if (str(board[i][j]) == sign):
                    CounterRow += 1
                    if (CounterRow == 3):
                        return True
                if (str(board[j][i]) == sign):
                    counterColumn += 1
                    if (counterColumn == 3):
                        return True
                if (i == 0):
                    if (str(board[j][k])==sign):
                        counterDiagonally += 1
                        if (counterDiagonally == 3):
                            return True
                if (i == 1):
                    if (str(board[0+j][2-k])==sign):
                        counterDiagonally += 1
                        if (counterDiagonally == 3):
                            return True
                    k += 1
    return False
                
            
# Funkcja, która dokonuje analizy stanu tablicy w celu sprawdzenia
# czy użytkownik/gracz stosujący "O" lub "X" wygrał rozgrywkę.
#
from random import randrange

def draw_move(board):
    print("Ruch bota!")
    free_moves = make_list_of_free_fields(board)
    BotMove = randrange(len(free_moves))
    i= free_moves[BotMove][0]
    j= free_moves[BotMove][1]
    board[i][j] = 'X'
    
# Funkcja, która wykonuje ruch za komputer i aktualizuje tablicę.


board_state = [[1,2,3],[4,5,6],[7,8,9]]
#board_state = [['O','O','O'],['O','O','O'],['O',8,9]]
free_moves = make_list_of_free_fields(board_state)

while (free_moves != 0):
    draw_move(board_state)
    display_board(board_state)
    if (free_moves == 0):
        print("Remis ;X")
        break
    if ( victory_for(board_state, 'X') == True):
        print("Bot wygral! ;C")
        break
    enter_move(board_state)
    display_board(board_state)
    if ( victory_for(board_state, 'O') == True):
        print("lol wygralem! ;>")
        break
