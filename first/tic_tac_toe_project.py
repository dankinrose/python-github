import random

def create_numbered_board():
    board = ["1", "2", "3",
             "4", "5", "6",
             "7", "8", "9"]
    return board

def print_board(board):
    print()
    print("Board:\n")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()


def check_winner(board):
    win_positions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for a, b, c in win_positions:
        if board[a] == board[b] == board[c]:
            return True
    return False

def check_draw(board):
    for cell in board:
        if cell not in ["X", "O"]:
            return False
    return True

def choose_game_mode():
    game_mode = input("\nChoose game mode:\nTo play against a real player press '1', to play against a computer press any other key:")
    if game_mode == "1":
        print("you have chosen to play against real player!")
    else:
        print("you have chosen to play against a computer!")
    return game_mode

def get_players_info():
    game_mode = choose_game_mode()
    if game_mode == "1":
        player1_name = input(f"\nplease enter name for player 1:")
        player2_name = input(f"please enter name for player 2:")
    else:
        player1_name = input(f"\nplease enter your name:")
        player2_name = "computer"
    player1_symbol = input(f"\n{player1_name} please choose your symbol (X/O) or press anything else for random choice:")
    player1_symbol = player1_symbol.upper()

    if player1_symbol not in ["X", "O"]:
        player1_symbol = random.choice(["X", "O"])
        print(f"\n{player1_name} you've got random symbol - '{player1_symbol}'")
        player2_symbol = "O" if player1_symbol == "X" else "X"
        print(f"so {player2_name} symbol is - '{player2_symbol}'")

    else:
        print(f"\n{player1_name} symbol is - '{player1_symbol}'")
        player2_symbol = "O" if player1_symbol == "X" else "X"
        print(f"so {player2_name} symbol is - '{player2_symbol}'")

    print("\nThe game is ready, have fun!")

    return player1_name, player1_symbol, player2_name, player2_symbol

def players_turn(player1_name, player1_symbol, player2_name, player2_symbol, player1_turn ):
    if player1_turn == True:
        name = player1_name
        symbol = player1_symbol
    else:
        name = player2_name
        symbol = player2_symbol

    return name, symbol

def player_move(board, name, symbol):
    while True:
        try:
            choice = int(input(f"{name} make your move! choose cell by entering number between 1 to 9:")) -1
            if choice < 0 or choice > 8:
                raise Exception("invalid index")

            if board[choice] in ["X", "O"]:
                raise Exception("This cell is already taken")

            else:
                    board[choice] = symbol
                    return choice

        except ValueError:
            print("\nInvalid input. please select a number within the specified range.\n")
        except Exception as error:
            print(f"\noops! {error}. please try again...\n")

def switch_turn(player1_turn):
    return not player1_turn

def play_game():
    print("\nwelcome to the tic tac toe game!")
    board = create_numbered_board()
    player1_name, player1_symbol, player2_name, player2_symbol = get_players_info()
    player1_turn = True

    while True:

        print_board(board)
        name, symbol = players_turn(player1_name, player1_symbol, player2_name, player2_symbol, player1_turn )

        if name == "computer":
            print(f"{name} is thinking....")
            available_cells = []

            for i in range(9):
                if board[i] != "X" and board[i] != "O":
                    available_cells.append(i)

            choice = random.choice(available_cells)
            board[choice] = symbol

        else:
            player_move(board, name, symbol)

        if check_winner(board):
            print_board(board)
            print(f"congratulations! {name} is the winner of the game!")
            return True

        if check_draw(board):
            print_board(board)
            print("it's a draw!")
            return True

        player1_turn = switch_turn(player1_turn)

def start_game():
    while True:
        game_ended = play_game()
        if game_ended:
            play_again = input("\nDo you want to play again? press Y for yes and anything else for no: ")
            play_again = play_again.upper()
            if not play_again == "Y":
                break

    print("\nGame ended")
    print("Thanks for playing Tic Tac Toe! Goodbye")


if __name__ == '__main__':
    start_game()