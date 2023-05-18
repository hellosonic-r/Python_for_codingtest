t = int(input())

for test_case in range(1,t+1):
    string = list(input())
    now = []
    d = {"S":13, "D":13, "H":13, "C":13}

    for i in range(len(string)//3): #i = 0,1,2,3
        d[string[3*i]] -= 1
        now.append("".join(map(str, string[3*i:3*i+3])))

    if len(list(set(now))) != len(string)//3:
        print("#{} {}".format(test_case, "ERROR"))

    else:
        print("#{} {} {} {} {}".format(test_case, d["S"],d["D"],d["H"],d["C"]))

