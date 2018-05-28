def print_header():
    print("---------------------------------------------")
    print("------Rock, Paper, Scissors------------------")
    print("---------------------------------------------")


import random, collections

WINNING = {"Scissors": "Paper", "Paper": "Rock", "Rock": "Scissors"}
COUNTS = []


def get_players_name():
    return input("What is your player name?: ")


class Player:
    def __init__(self, name):
        self.name = name


def game_loop(player1, player2):
    count = 0
    while count < 3:
        p2_roll = random.sample(list(WINNING), 1)[0]  
        print(p2_roll)
        p1_roll = input("Pick [R]ock, [P]aper or [S]cissors: ")
        if p1_roll.upper() == "R":
            p1_roll = "Rock"
        elif p1_roll.upper() == "P":
            p1_roll = "Paper"
        elif p1_roll.upper() == "S":
            p1_roll = "Scissors"
        else:
            print("Not a valid option")

        if p1_roll == p2_roll:
            print("tie")
            COUNTS.append('tie')
        elif p1_roll in WINNING:
            print('Yay')
            COUNTS.append(player1.name)
        else:
            print('you lost')
            COUNTS.append(player2.name)
        count += 1
    final = collections.Counter(COUNTS)
    final = final.most_common()
    print(final)
    if final[0][0] == player1.name:
        print('You won!!!')
    elif final[0][0] == player2.name:
        print('The computer won')
    else:
        print("It's a tie")


def main():
    print_header()

    name = get_players_name()

    player1 = Player(name)
    player2 = Player("computer")

    game_loop(player1, player2)


main()
