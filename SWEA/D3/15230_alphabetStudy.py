t = int(input())
for test_case in range(1, t+1):
    string = list(input())
    cnt = 0
    j = 0
    for i in range(len(string)):
        if ord(string[i]) == 97 + j:
            cnt += 1
            j += 1
        else:
            break
    print("#{} {}".format(test_case, cnt))