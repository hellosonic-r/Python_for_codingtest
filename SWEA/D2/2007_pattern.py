t = int(input())
for test_case in range(1, t+1):
    string = list(input())
    check = []
    i = 0
    while True:
        check.append(string.pop(0))
        i += 1
        if check == string[:i]:
            break
    print("#{} {}".format(test_case, i))
