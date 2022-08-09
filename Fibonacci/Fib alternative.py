def fib(a, b):
    if b < 1:
        return a * -b
    else:
        return fib(a, b - 1) + fib(a, b - 2)


def lst_fib(x, y):
    lst = []
    for i in range(y):
        lst.append(fib(x, i))
    print(lst)


def enum_fib(l, m):
    for i in range(m):
        print(fib(l, i))


while True:
    try:
        n = int(input("First no.: "))
        o = int(input("Fib Length: "))
    except ValueError:
        print("\nInteger only\n")
        continue
    do = input("""\nList Fibonacci[1]
Enumerate Fibonacci[2]

>""")
    if do == "1":
        lst_fib(n, o)
    elif do == "2":
        enum_fib(n, o)
    else:
        print("1 or 2")