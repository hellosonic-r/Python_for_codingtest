#sys 라이브러리 / sys.stdin.readline().split() 사용으로 시간 단축

import sys

t = int(input())

for _ in range(t):
    num = list(map(int, sys.stdin.readline().split()))
    num.sort()
    print(num[-3])