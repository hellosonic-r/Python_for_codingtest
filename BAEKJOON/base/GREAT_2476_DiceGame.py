import sys 

N = int(input())
prize_list = []
for i in range(N):
    a, b, c = map(int, sys.stdin.readline().split())

    if a == b == c:
        prize = 10000 + a * 1000
        prize_list.append(prize)
    elif a == b and a != c:
        prize = 1000 + a * 100
        prize_list.append(prize)
    elif a == c and a != b:
        prize = 1000 + a * 100
        prize_list.append(prize)
    elif b == c and a != b:
        prize = 1000 + b * 100
        prize_list.append(prize)
    else:
        prize = max(a,b,c) * 100
        prize_list.append(prize)

print(max(prize_list))

