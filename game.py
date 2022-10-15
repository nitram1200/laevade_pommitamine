import numpy as np
from random import randint


# Rules
def rules():
    print('Rules:\n')
    print('Ships')
    print('There are a total of 5 ships:')
    print('Carrier, takes up 5 spaces and is notated with "C".')
    print('Battleship, takes up 4 spaces and is notated with "B".')
    print('Destroyer, takes up 3 spaces and is notated with "D".')
    print('Submarine, takes up 3 spaces and is notated with "S".')
    print('Patrol boat, takes up 2 spaces and is notated with "P".\n')
    print('Placement of ships')
    print("Ships can't overlap or touch each other")
    print('To select a spot on the grid choose the corresponding letter of the row and then number')
    print('Examples of inputs: "A1", "H10", "C9".')
    print('To enter the location of your ship, you need to give 2 inputs - beginning and end squares of the ship.')
    print('Example of placing a Destroyer on squares B2, C2, D2 would need the input of just B2 and D2.')
    print('If you mess up or want to change the potion of your ship you will have that change, so no need to worry.\n')
    print('Making turns')
    print('The player always gets the first turn of the game.')
    print('Amount of shots depends on how meany ships you still have left (That includes partially destroyed ships).')
    print('So you your carrier has been sunk and patrol boat has been hit once, then you get 4 turns.')
    print('The game ends when all of the enemy ships have been destroyed.')


rules()


# Global variables
def initiate():
    board = [  # Blank play area
        [" ", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
        ["a", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["b", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["c", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["d", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["e", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["f", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["g", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["h", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["i", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["j", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"]
    ]
    ships = {
        "carrier": [5, False],
        "battleship": [4, False],
        "destroyer": [3, False],
        "submarine": [3, False],
        "patrol boat": [2, False]
    }
    player_ships = {"C": 5,
                    "B": 4,
                    "D": 3,
                    "S": 3,
                    "P": 2}
    pc_ships = {"C": 5,
                "B": 4,
                "D": 3,
                "S": 3,
                "P": 2}
    markers = ["C", "B", "D", "S", "P"]
    allowed_chars = [" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    np_board_player = np.array(board)
    np_board_player_public = np.array(board)
    np_board_pc = np.array(board)
    np_board_pc_public = np.array(board)
    return board, ships, player_ships, pc_ships, markers, allowed_chars, np_board_player, np_board_player_public, np_board_pc, np_board_pc_public


player_score = 0
pc_score = 0


# Setup functions
def switch_inputs_2(a, b):
    return a, b


def switch_inputs_4(a, b, c, d):
    return a, b, c, d


def test_input(x):
    if x[0] in allowed_chars:
        if (x[1:]).isdigit():
            if int(x[1:]) < 11:
                return True
            else:
                print("Make sure you didn't leave spaces and the ship is on the board")
        else:
            print("Make sure you didn't use spaces and that only the first character is a letter")
    else:
        print("Make sure the first character is a letter and you didn't leave spaces.")

    return False


def test_len(x, y, l):
    if x[0] == y[0]:
        if int(y[1:]) - int(x[1:]) == l:
            return True

        elif int(y[1:]) - int(x[1:]) < l:
            print("Your ships is too small. Try again.")
        elif int(y[1:]) - int(x[1:]) > l:
            print("Your ship is too big. Try again.")

        return False

    if int(y[1:]) != int(x[1:]):
        print("The ship must be on the same column or row.")

    else:
        if int(allowed_chars.index(y[0])) - int(allowed_chars.index(x[0])) == l:
            return True

        elif int(allowed_chars.index(y[0])) - int(allowed_chars.index(x[0])) > l:
            print("Your ship is too small. Try again.")
        elif int(allowed_chars.index(y[0])) - int(allowed_chars.index(x[0])) < l:
            print("Your ship is too big. Try again.")

    return False


def test_loc(x, y, ship):
    for s in ships.keys():
        if s[0].upper() in np_board_player[int(allowed_chars.index(x[0])) - 1:int(allowed_chars.index(y[0])) + 2, int(x[1]) - 1:int(y[1]) + 2]:
            print("You can't overlap existing ships.")
            return False

    np_board_player[int(allowed_chars.index(x[0])):int(allowed_chars.index(y[0])) + 1, int(x[1:]):int(y[1:]) + 1] = str(
        ship[0]).upper()
    return True


def create_ships_player():
    global np_board_player

    for x, y in ships.items():
        print("Place your " + x + " (" + str(y[0]) + " spaces)")
        while ships[x][1] is False:

            print(np_board_player)
            happy = False
            start = input("Where does your " + x + " start?").upper()

            if test_input(start):
                end = input("Where does your " + x + " end?").upper()

                if test_input(end):

                    if int(start[1:]) > int(end[1:]) or int(allowed_chars.index(start[0])) > int(
                            allowed_chars.index(end[0])):
                        end, start = switch_inputs_2(start, end)

                    if test_len(start, end, ships[x][0] - 1):

                        if test_loc(start, end, x):

                            while happy is False:
                                print(np_board_player)
                                happy_ = input("Are you happy with the placement of the " + x + " ? (yes/no) ").lower()

                                if happy_ == "yes" or happy_ == "y":
                                    happy = True
                                    ships[x][1] = True

                                elif happy_ == "no" or happy_ == "n":
                                    happy = True
                                    np_board_player[int(allowed_chars.index(start[0])):int(allowed_chars.index(end[0])) + 1, int(start[1:]):int(end[1:]) + 1] = "O"
                                else:
                                    print("Sorry I couldn't understand you, please repeat.")

    print(np_board_player)

    happy = False
    while happy is False:
        happy = input("Are you happy with the placement of your ships? (yes/no) ").lower()
        if happy == "yes" or happy == "y":
            return

        elif happy == "no" or happy == "n":
            sure = input("Are you sure, this will reset the whole board? (yes/no) ").lower()
            if sure == "yes" or sure == "y":
                np_board_player = np.array(board)  # Resets the whole board
                create_ships_player()
            elif sure == "no" or sure == "n":
                return
        else:
            print("Sorry, I couldn't understand you, please repeat")


def pc_input(l):
    check = False

    while check is False:
        start_letter = randint(1, 10)
        start_number = randint(1, 10)

        for r in range(6):
            direction = randint(1, 4)
            end_letter = start_letter
            end_number = start_number

            if direction > 2:
                if direction == 4:
                    end_letter = start_letter + l - 1
                else:
                    end_letter = start_letter - l + 1
            else:
                if direction == 2:
                    end_number = start_number + l - 1
                else:
                    end_number = start_number - l + 1

            if end_letter in range(1, 11) and end_number in range(1, 11):
                break

        if \
                r < 5:
            if start_letter > end_letter or start_number > end_number:
                end_letter, start_letter, end_number, start_number = switch_inputs_4(start_letter, end_letter,
                                                                                     start_number, end_number)

            return start_letter, end_letter, start_number, end_number


def create_ships_pc():
    for x, y in ships.items():
        pc_ship = False

        while pc_ship is False:
            loc = False
            check = True
            start_letter, end_letter, start_number, end_number = pc_input(y[0])

            while loc is False:
                for s in ships.keys():
                    if s[0].upper() in np_board_pc[start_letter - 1:end_letter + 2, start_number - 1:end_number + 2]:
                        check = False
                        break
                loc = True

            if check is True and loc is True:
                np_board_pc[start_letter:end_letter + 1, start_number:end_number + 1] = str(x[0]).upper()
                pc_ship = True


# Turn functions
def print_boards(x, y):
    print("Computers board:                                 Your board:")
    line = 0
    for l in x:
        print(l, "  ", y[line])
        line += 1


def targeting_system(targets, p):
    hits = []
    global pc_ships
    global player_ships

    if p == "player":
        if len(targets) > 1:
            for t in targets:
                if np_board_pc[int(allowed_chars.index(t[0])), int(t[1:])] in markers:
                    hits.append([t, np_board_pc[int(allowed_chars.index(t[0])), int(t[1:])]])
                    np_board_pc_public[int(allowed_chars.index(t[0])), int(t[1:])] = np_board_pc[
                        int(allowed_chars.index(t[0])), int(t[1:])]
                else:
                    np_board_pc_public[int(allowed_chars.index(t[0])), int(t[1:])] = "X"
        else:
            if np_board_pc[int(allowed_chars.index(targets[0][0])), int(targets[0][1:])] in markers:
                hits.append([targets[0], np_board_pc[int(allowed_chars.index(targets[0][0])), int(targets[0][1:])]])
                np_board_pc_public[int(allowed_chars.index(targets[0][0])), int(targets[0][1:])] = np_board_pc[
                    int(allowed_chars.index(targets[0][0])), int(targets[0][1:])]

        if len(hits) > 1:
            print(len(hits), "shots landed on enemy ships located at:")
            for h in hits:
                print(h[0])
                pc_ships[h[1]] -= 1
        elif len(hits) == 1:
            print("1 shot landed on an enemy ship located at:", hits[0][0])
            pc_ships[hits[0][1]] -= 1
        elif len(hits) == 0:
            print("You missed all of your shots")

        pc_ships = {key: value for (key, value) in pc_ships.items() if value > 0}

    else:
        print(targets)
        if len(targets) > 1:
            for t in targets:
                if np_board_player[t[0], t[1]] in markers:
                    np_board_player_public[t[0], t[1]] = np_board_player[t[0], t[1]]
                    hits.append([str(allowed_chars[t[0]]) + str(t[1]), np_board_player_public[t[0], t[1]]])
                else:
                    np_board_player_public[t[0], t[1]] = "X"
        else:
            if np_board_player[targets[0][0], targets[0][1:]] in markers:
                np_board_player_public[targets[0], targets[1]] = np_board_player[targets[0][0], targets[0][1]]
                hits.append([str(allowed_chars[targets[0]]) + str(targets[1]),
                             np_board_player_public[targets[0][0], targets[0][1]]])
            else:
                np_board_player_public[targets[0][0], targets[0][1]] = "X"

        if len(hits) > 1:
            print("Computer hit", len(hits), "ships on squares:")
            for h in hits:
                print(h[0])
                player_ships[h[1]] -= 1
        elif len(hits) == 1:
            print("Computer hit 1 ship on square:", hits[0][0])
            player_ships[hits[0][1]] -= 1
        elif len(hits) == 0:
            print("Computer missed all of its shots.")

        player_ships = {key: value for (key, value) in player_ships.items() if value > 0}

    return hits


def attack(ships, player):
    targets = []
    hits = len(ships)
    print(hits)

    for x in ships.keys():

        if player == "player":
            player_input = False
            print("You can hit", hits, "more targets.")

            while player_input is False:
                target = input("Where would you like to hit?").upper()

                if test_input(target):
                    if np_board_pc_public[int(allowed_chars.index(target[0])), int(target[1:])] == "O":
                        if target not in targets:
                            targets.append(target)
                            hits -= 1
                            player_input = True
                        else:
                            print("You already hit that place this turn. Try again.")
                    else:
                        print("You have already hit that place")

        else:
            pc_in = False
            print(x)

            while pc_in is False:
                letter = randint(1, 10)
                number = randint(1, 10)

                if np_board_player_public[letter, number] == "O":
                    if [letter, number] not in targets:
                        pc_in = True
                        targets.append([letter, number])

    return targets


def battle_system():
    alive = True
    player_turn = True
    pc_turn = False
    turn = 1

    while alive is True:

        while player_turn is True:
            print("Current turn:", turn)
            print(player_ships)

            print_boards(np_board_pc_public, np_board_player_public)

            targets = attack(player_ships, "player")
            targeting_system(targets, "player")
            turn += 1

            if len(pc_ships) == 0:
                return "player"
            elif len(player_ships) == 0:
                return "pc"

            player_turn = False
            pc_turn = True

        while pc_turn is True:
            print("Current turn:", turn)
            print(pc_ships)
            targets = attack(pc_ships, "pc")
            targeting_system(targets, "pc")
            turn += 1

            if len(pc_ships) == 0:
                return "player"
            elif len(player_ships) == 0:
                return "pc"

            pc_turn = False
            player_turn = True


# Main function
def match():
    global player_score, pc_score, board, ships, player_ships, pc_ships, markers, allowed_chars, np_board_player, np_board_player_public, np_board_pc, np_board_pc_public
    board, ships, player_ships, pc_ships, markers, allowed_chars, np_board_player, np_board_player_public, np_board_pc, np_board_pc_public = initiate()
    create_ships_player()
    create_ships_pc()
    result = battle_system()

    if result == "player":
        print("Congratulations, you won!!!")
        player_score += 1
    else:
        print("Sorry, you lost, better luck next time!")
        pc_score += 1

    print("Your score:", player_score)
    print("Computer score:", pc_score)
    rematch = False

    while rematch is False:
        re = input("Do you want to play again? (yes/no)").lower()

        if re == "yes" or re == "y":
            match()
        elif re == "no" or re == "n":
            return
        else:
            print("Sorry I couldn't understand you, please try again. ")


match()
