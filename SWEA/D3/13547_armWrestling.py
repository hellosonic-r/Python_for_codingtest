t = int(input())

for test_case in range(1, t+1):
    vic = list(input())
    cnt = 0
    for i in range(len(vic)):
        if vic[i] == "x":
            cnt += 1
    if 15 - cnt >=8:
        print("#{} {}".format(test_case, "YES"))
    else:
        print("#{} {}".format(test_case, "NO"))