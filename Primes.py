def is_prime(x):
    try:
        x = int(x)
        if x % 2 == 0 and x!=2 or x % 3 == 0 and x!=3 or x % 5 == 0 and x!= 5 or x % 7 == 0 and x!=7:
            return False
        else:
            return True
    except ValueError:
        return False


def more_prime(x, y):
    for i in range(x, y):
        if is_prime(i):
            yield i
            i += 1
        else:
            i += 1
            continue


while True:
    a = input("""\nWhat do you want to do :
    Find out if a number is Prime(1)
    List Prime numbers in a range(2)
    END(3)
    
>""")

    if a == "1":
        g = input("\nNumber : ")
        if is_prime(g):
            print(g, " is a Prime number.")
            continue
        else:
            print(g, " is not a Prime number.")
            continue

    elif a == "2":
        fro = int(input("From: "))
        t = int(input("To: "))
        print("\n", list(more_prime(fro, t)))
        continue
    elif a == "3" or a == "end" or a == "END" or a == "End":
        break
    else:
        print("\nWhat?")
