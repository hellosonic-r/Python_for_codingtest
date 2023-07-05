a = input()
b = input()
a = [""] + list(map(str, str(a)))
b = [""] + list(map(str, str(b)))
n = max(len(a),len(b)) - 1
idx = 0
start = 1
max_ans = 0
ans = 0
while start < len(a):
    dp = [0] * (n + 2)
    for i in range(start, len(a)):
        for j in range(1, len(b)):
            if a[i] == b[j] and j>idx:
                dp[j] = max(dp[:j])+1
                idx = j
                break
    start+=1
    ans = max(dp)
    if max_ans < ans:
        max_ans = ans

print(max_ans)


