while True:
    line = input()
    if line == "0 0":
        break
    else:
        A, B = map(int, line.split())
        print(A + B)