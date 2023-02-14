import sys

n = int(input()) #라운드 수

a_score, b_score = 100, 100

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    if a > b:
        a_score = a_score
        b_score -= a
    elif a < b:
        a_score -= b
        b_score = b_score
    else:
        continue
print(a_score, b_score, sep = "\n")