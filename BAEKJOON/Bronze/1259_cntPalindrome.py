while True:
    n = list(map(int, str(input())))
    if n == [0]:
        break
    if n == n[::-1]:
        print("yes")
    else:
        print("no")
    