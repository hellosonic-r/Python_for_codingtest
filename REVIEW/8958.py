import sys

n = int(input())
for i in range(n):
    score = 0
    result = 0
    q = list(sys.stdin.readline())
    for j in range(len(q)):
        if q[j] == "O":
            score += 1
            result += score
        else:
            score = 0
    print(result)
