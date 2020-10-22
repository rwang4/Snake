import random


def printgame(p1, p2):
    print("*"*40)
    print("Player x: ", ' '.join(p1))
    print("Player o: ", ' '.join(p2))
    print("*"*40)


def main():
    p1 = ['x', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
    p2 = ['o', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
    idx1 = 0
    idx2 = 0
    l = len(p1)
    turn = 0
    printgame(p1, p2)
    print("Players begin in the starting position")
    while(1):
        if turn == 0:
            input("Player x press enter to roll!")
            roll = random.randint(1, 6)
            print("Player x rolled a", roll)
            p1[idx1] = '-'
            idx1 += roll
            if idx1 >= l:
                print("The roll was too high, player x has been sent to the start")
                idx1 = 0
                p1[idx1] = 'x'
            p1[idx1] = 'x'
            printgame(p1, p2)
            if idx1 == l-1:
                print("Player x has won!")
                break
            turn = 1
        else:
            input("Player o press enter to roll!")
            roll = random.randint(1, 6)
            print("Player o rolled a", roll)
            p2[idx2] = '-'
            idx2 += roll
            if idx2 >= l:
                print("The roll was too high, player o has been sent to the start")
                idx2 = 0
                p2[idx2] = 'o'
            p2[idx2] = 'o'
            printgame(p1, p2)
            if idx2 == l-1:
                print("Player o has won!")
                break
            turn = 0


main()
