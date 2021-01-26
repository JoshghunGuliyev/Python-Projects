num_table = " 7 | 8 | 9 \n-----------\n 4 | 5 | 6 \n-----------\n 1 | 2 | 3 "
user_table = "   |   |   \n-----------\n   |   |   \n-----------\n   |   |   "
winner_line = "'132','456','789','147','258','369','159','357'"
empty_cells = '123456789'
winner = ""

def clear_table():
    global user_table, winner_line, empty_cells, winner, game
    user_table = "   |   |   \n-----------\n   |   |   \n-----------\n   |   |   "
    winner_line = "'132','456','789','147','258','369','159','357'"
    empty_cells = '123456789'
    winner = ""
    game = 'Y'

def new_game():
    global game
    game = input("Play again? Y / N: ")
    while game not in ['Y','N']:
        game = input("Please type Y for new game or N for stop: ")
    return game

def check_winner():
    global winner
    if 'XXX'in winner_line:
        print("CONGURATILATIONS! Player 1 WINS! ")
        winner = "Player 1"
    elif 'OOO'in winner_line:
        print("CONGURATILATIONS! Player 2 WINS! ")
        winner = "Player 2"
    elif empty_cells == "":
        print("Game over! No one wins!")
        winner = "No one"
    else: pass

def begin_game():
    global game
    game = 'Y'
    print("Let's begin!")
    print("\nHere is the Tic_Tac_Toe table !\n")
    print(user_table + "\n")
    rules = input("Do you want to know how to play? - Yes o No : ")

    while rules not in ['Yes', 'No']:
        print("Please type Yes or No, same as written here")
        rules = input("Do you want to know how to play? - Yes o No : ")

    if rules == 'Yes':
        print("------------------------------------------------------------------------------------")
        print("\nSo, according to below numpad you will choose where to put your 'X' or 'O'\n")
        print(num_table + "\n")
    else:
        pass

    xo = input("OK, let's start. Do you want X or O : ")
    while xo not in ['X', 'O']:
        print("Pelase type X or O to choose")
        xo = input("OK, let's start. Do you want X or O : ")

    if xo == 'X':
        print("OK, Great, you are Player 1 and you'll start first")
    else:
        print("OK, Great, you are Player 2 and you'll start second")

def player1_choice():
    global user_table, winner_line, empty_cells, winner
    if winner == "":
        player1 = input("Player 1, in which position do you want to place 'X' ?: ")
        while player1 not in str(list(range(1,10))):
            player1 = input("Player 1, Remember rules! You should choose a number between 1 and 9: ")
        place = num_table.find(player1)
        user_table = list(user_table)
        while user_table[place] != " ":
            player1 = input("OOPS! This position if full, please choose another one! : ")
            place = num_table.find(player1)
        user_table[place] = "X"
        user_table = str(''.join(user_table))
        empty_cells = empty_cells.replace(player1,'')
        winner_line = winner_line.replace(player1,'X')
        print(user_table)
    else: pass

def player2_choice():
    global user_table, winner_line, empty_cells, winner
    if winner == "":
        player2 = input("Player 2, in which position do you want to place 'O' ?: ")
        while player2 not in str(list(range(1,10))):
            player2 = input("Player 2, Remember rules! You should choose a number between 1 and 9: ")
        place = num_table.find(player2)
        user_table = list(user_table)
        while user_table[place] != " ":
            player2 = input("OOPS! This position if full, please choose another one! : ")
            place = num_table.find(player2)
        user_table[place] = "O"
        user_table = str(''.join(user_table))
        empty_cells = empty_cells.replace(player2,'')
        winner_line = winner_line.replace(player2,'O')
        print(user_table)
    else: pass

def TTT():
    begin_game()
    while game == 'Y':
        while winner == "":
            player1_choice()
            check_winner()
            player2_choice()
            check_winner()
        clear_table()
        new_game()
    clear_table()

TTT()