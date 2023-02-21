# r : 광고를 하지 않았을 때 수익
# e : 광고를 했을 때 수익
# c : 광고 비용

import sys

N = int(input())
for i in range(N):
    r, e, c = map(int, sys.stdin.readline().split())
    print("advertise" if e>r+c else("do not advertise" if e<r+c else "does not matter"))
