import random
while True:
    g = input("Would you like to play a guessing game [y/n]? : ")
    if g=="y":
        r=int(input("Number Guessing. Choose a max number: [10, 100, 1000] : "))
        if r==10 or r==100 or r==1000:
            n =random.randint (1,r)
            score=20
    elif g=="n":
        print("OK, next time then")
        break
    else:
        print("What?")
        continue
    while True:
        x=input("Guess the number between 1 and "+str(memoryview)+" : ")
        if x.isdigit()!=True:
            print("That is not a number(-2 pts)")
            score -= 2
        elif int(x)==n and int(x)==69:
            print("Correct! what are the chances?")
            print("Score="+str(score))
        elif int(x) == n:
            print("Yes the number is " + str(n))
            print("Your score is: " +str(score))
            break
        elif int(x)==69:
            print("Nice but still wrong")
        elif int(x)>r or int(x)<1:
            print("Only numbers between 1 and "+ str(r) +"(-2pts)")
            score-=2
        elif int(x)<n:
            print("Higher")
            score-=1
        elif int(x)>n:
            print("Lower")
            score-=1
    print("New game? [y/n]")
    g=input()
    if g=="y":
        continue
    else:
        print("Goodbye!")



