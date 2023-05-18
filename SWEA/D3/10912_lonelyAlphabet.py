t = int(input())

for test_case in range(1,t+1):
    string = list(map(str, str(input())))
    string.sort()

    #a:97 z:122
    ans = ""
    for i in range(97,123):
        if string.count(chr(i)) % 2 == 1:
            if chr(i) not in ans:
                ans += chr(i)
            else:
                continue
        else:
            continue

    if ans == "":
        print("#{} {}".format(test_case, "Good"))
    else:
        print("#{} {}".format(test_case, ans))

