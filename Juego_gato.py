def draw_board(board):
    print("\n")
    print("   |   |")
    print(" "+board[6]+" | "+board[7]+" | "+board[8])
    print("___|___|___")
    print("   |   |")
    print(" "+board[3]+" | "+board[4]+" | "+board[5])
    print("___|___|___")
    print("   |   |")
    print(" "+board[0]+" | "+board[1]+" | "+board[2])
    print("   |   |")

def check_winner(board, player):
    if (board[0] == player and board[1] == player and board[2] == player) or \
       (board[3] == player and board[4] == player and board[5] == player) or \
       (board[6] == player and board[7] == player and board[8] == player) or \
       (board[0] == player and board[3] == player and board[6] == player) or \
       (board[1] == player and board[4] == player and board[7] == player) or \
       (board[2] == player and board[5] == player and board[8] == player) or \
       (board[0] == player and board[4] == player and board[8] == player) or \
       (board[2] == player and board[4] == player and board[6] == player):
        return True
    else:
        return False
    
def show_winners(winners):
    str(winners)
    print("\nX gano",winners.count("X"),"veces y O ganó",winners.count("O"))

def play_game(winner):
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    player1 = "X"
    player2 = "O"
    if winner == "X": current_player = "O"
    else: current_player = "X"

    print("\nBienvenido al juego del gato, este es el tablero:")
    draw_board(board)
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
  
    for i in range(9):
        print("\nEs el turno de "+current_player)
        move = input("Has tu movimiento: ")
        if move not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
          print("Movimiento no valido, intenta otro.")
          i-=1
          continue
          
        elif board[int(move)-1] == "X" or board[int(move)-1] == "O":
            print("Ya esta ocupado, intenta otro.")
            i-=1
            continue
          
        else:
            board[int(move)-1] = current_player
            draw_board(board)
          
            if check_winner(board, current_player):
                print("Felicidades "+current_player+" ganaste!")
                return current_player
            
            if current_player == player1:
                current_player = player2
            else:
                current_player = player1
    else:
        print("Empate")
        return " "

winners = []
player = ""
while True:
    winner = play_game(player)
    if winner != " ":
        winners.append(winner)
        player = winner
    seguir = input("\nQuieres seguir jugando? (no=0)")
    if seguir == "0":
        show_winners(winners)
        break