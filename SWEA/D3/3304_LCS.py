t = int(input())

for test_case in range(1, t+1):
    a, b = map(str, input().split())
    a = [""] + list(map(str, str(a)))
    b = [""] + list(map(str, str(b)))
    n = max(len(a),len(b)) - 1
    dp = [0] * (n+2)
    idx = 0
    for i in range(1, len(a)):
        for j in range(1, len(b)):
            if a[i] == b[j] and j>idx:
                dp[j] = max(dp[:j])+1
                idx = j
                break

    print("#{} {}".format(test_case, max(dp)))

