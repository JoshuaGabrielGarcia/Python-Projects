def is_prime(x):
    try:
        x = int(x)
        for i in range(2, 8):
            if x % i == 0 and x != i:
                return False
        return True
    except ValueError:
        return False


def more_prime(x, y):
    for i in range(x, y+1):
        if is_prime(i):
            yield i
        else:
            i += 1
            

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
