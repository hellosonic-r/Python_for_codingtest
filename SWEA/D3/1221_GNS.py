t = int(input())
for test_case in range(1,t+1):
    test_num, n = input().split()
    string = list(map(str, input().split()))
    d = {"ZRO":0, "ONE":1, "TWO":2, "THR":3, "FOR":4, "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9}

    string.sort(key = lambda x: d[x])

    print("#{}".format(test_case))
    print(" ".join(map(str, string)))