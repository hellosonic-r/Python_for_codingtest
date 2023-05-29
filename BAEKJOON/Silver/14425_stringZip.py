n, m = map(int, input().split())

string = []

for _ in range(n):
    string.append(input())

cnt = 0
for i in range(m):
    if input() in string:
        cnt += 1

print(cnt)