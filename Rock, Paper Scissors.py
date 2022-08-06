import random
while True:
    p = input("Rock, Paper, Scissors? [y/n]: ")
    cnt = 0
    if p != "y" and p != "n":
        print("'y' or 'n' ONLY")
        cnt += 1
        p = input()
        if p != "y" and p != "n":
            cnt += 1
            p = input("y OR n : ")
            if p != "y" and p != "n":
                cnt += 1
                p = input("Are you messing with me? [y/n] : ")
                while p != "y" and p != "n":
                    cnt += 1
                    p = input("Answer the QUESTION. [y/n] : ")
                if p == "y" or p == "Y" or p == "yes" or p == "Yes" or p == "YES":
                    print("Screw you then!")
                    break
                elif p == "n" or p == "N" or p == "No" or p == "no":
                    print("Oh, ok then.")
                    print("Maybe you just miss clicked " + str(cnt) + " times")
                    continue
    elif p == "y":
        while True:
            opp = random.randint(1, 3)
            ans = input("Rock, Paper, Scissors : ")
            if ans == "Rock" or ans == "rock" or ans == "R" or ans == "r":
                if opp == 1:
                    print('Rock')
                    print("It's a Tie")
                    continue
                elif opp == 2:
                    print("Paper")
                    print("Paper beats rock, I win!")
                elif opp == 3:
                    print("Scissors")
                    print("Rock Beats Scissors, You win.")
            elif ans == "Paper" or ans == "paper" or ans == "P" or ans == "p":
                if opp == 1:
                    print('Rock')
                    print("Paper beats Rock, You win.")
                elif opp == 2:
                    print("Paper")
                    print("It's a Tie!")
                    continue
                elif opp == 3:
                    print("Scissors")
                    print("Scissors beats Paper, I win!")
            elif ans == "Scissors" or ans == "scissors" or ans == "S" or ans == "s":
                if opp == 1:
                    print('Rock')
                    print("Rock beats Scissors, I win!")
                elif opp == 2:
                    print("Paper")
                    print("Scissors beat Paper, You win")
                elif opp == 3:
                    print("Scissors")
                    print("It's a Tie")
                    continue

            ag = input("Again? [y/n]")
            if ag == "y":
                continue
            elif ag == "n":
                print("Ohhh Keeeey, Byeeeee")
                break
            else:
                print("What?")
                print("y/n only")
                while True:
                    ag = input("Again? [y/n]: ")
                    if ag != "y" and ag != "n":
                        print("y or n ONLY")
                    else:
                        break
                if ag == "y":
                    continue
                else:
                    break
        break
    elif p == "n":
        print("Ok, see you later")
        break
