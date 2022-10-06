import os

def comp(count):
    global board, sumbols

    turn = []
    computer = sumbols[count % 2]
    player = sumbols[(count - 1) % 2]

    for string in range(3):
        for column in range(3):
            if board[string][column] == " ":
                board[string][column] = computer
                if win() == computer:
                    return
                board[string][column] = player
                if win() == player:
                    turn = [string, column]
                board[string][column] = " "
    if len(turn) == 2:
        board[turn[0]][turn[1]] = computer
        return

    if board[1][1] == " ":
        board[1][1] = computer
        return

    for string in range(3):
        for column in range(3):
            if board[string][column] == " ":
                board[string][column] = computer
                return


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def start():
    global board
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

def print_game(a):
    global board
    print('-' * 7)
    for i in range(9):
        if i % 3 == 0:
            print('|', end="")
        if a == 'n' and board[i//3][i%3] == ' ':
            print(i + 1, end="|")
        else:
            print(board[i//3][i%3], end="|")
        if (i+1) % 3 == 0:
            print('\n-------')

def win():
    global board
    # horizontal and vertical
    for i in range(3):
        if ((board[i][0] == board[i][1] == board[i][2]) or (board[0][i] == board[1][i] == board[2][i])) and board[i][
        i] in ['x', 'o']:
            return board[i][i]
    # diagonals
    if ((board[0][0] == board[1][1] == board[2][2]) or (board[2][0] == board[1][1] == board[0][2])) and board[1][1] in [
        'x', 'o']:
        return board[1][1]
    for i in board:
        if ' ' in i:
            return None
    return "Ничья!"

def player(sumbol):
    global board
    print_game('n')
    point = int(input("Напишите номер ячейки: ").strip()) - 1
    if 0 > point or point > 8 or board[point//3][point%3] in ['x', 'o']:
        print("ERROR! Please, try again!")
        player(sumbol)
    else:
        board[point//3][point%3] = sumbol

board = list()
game = "да"
count = 0
sumbols = ['x', 'o']
while game == "да":
    start()
    while win() is None:
        if count % 2 == 0:
            player(sumbols[count % 2])
            clear()
            count += 1
        else:
            comp(count)
            clear()
            count += 1
    print_game('')
    if win() == "Ничья!":
        print(win())
    else:
        print("Победил игрок: " + win() + "!")
    game = input("Ещё раз? ").strip().lower()
