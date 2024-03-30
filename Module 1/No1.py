def cetakSiku(x):
    for i in range(1, x + 1):
        for j in range(i):
            print("*", end="")
        print()

cetakSiku(5)