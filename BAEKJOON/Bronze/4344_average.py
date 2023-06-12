import sys

t = int(input())
for test_case in range(1,t+1):
    score = list(map(int, sys.stdin.readline().split()))
    n = score[0]
    average = sum(score[1:]) / n
    cnt = 0
    for i in range(1,n+1):
        if score[i] > average:
            cnt += 1
    ans = round(cnt/n*100,3)
    print("{:.3f}{}".format(ans,"%"))

