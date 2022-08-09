def fib(x, y):
    lst=[]
    for i in range(y):
        if i > 1:
            lst.append(lst[i-1] + lst[i-2])
        else:
            lst.append(i * x)
    print("\n", lst, "\n")


while True:
    ans = input("""What to do?:
Original Fibonacci[1]
Edit Fibonacci[2]
End[3]

>""")
    try:
        ans = int(ans)
    except ValueError:
        print("Numbers only")
        continue
    if ans == 1:
        try:
            lngt = int(input("Fibonacci no. lenght: "))
            fib(1, lngt)
            continue
        except ValueError:
            print("Integers only")
    elif ans == 2:
        try:
            str = int(input("Fibonacci no. start: "))
            lngt = int(input("Fibonacci no. length: "))
            fib(str, lngt)
            continue
        except ValueError:
            print("Numbers only")
            continue

    else:
        break