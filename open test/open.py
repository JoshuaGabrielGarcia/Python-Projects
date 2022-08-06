while True:
    do = input("Append or Write : ")
    if do == "append" or do == "a" or do == "A":
        li = input("Newline : ")
        if li == "yes" or li == "y":
            file = open("Open_test.txt", "a")
            print("bytes = ", file.write("\n" + str(input("Text : "))))
            file.close()
        elif li == "no" or li == "n":
            file = open("Open_test.txt", "a")                                              
            print("bytes = ", file.write(" ", str(input("Text : "))))
            file.close()
        else:
            print("What?")
            continue

    elif do == "write" or do == "w" or do == "W":
        file = open("Open_test.txt", "w")
        print("bytes = ", file.write(str(input("Text : "))))
        file.close()
    else:
        continue
    file = open("open_test.txt", "r")
    print(file.read())
    file.close()
