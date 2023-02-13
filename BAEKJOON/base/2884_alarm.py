import sys

H, M = map(int, sys.stdin.readline().split())

if M <= 44 and H != 0:
    M = M + 15
    H = H - 1
    print(H,M)
elif M == 45:
    M = 0
    H = H
    print(H,M)
elif H == 0 and M <= 44:
    M = M + 15
    H = 23
    print(H,M)
else:
    M = M - 45
    H = H
    print(H,M)