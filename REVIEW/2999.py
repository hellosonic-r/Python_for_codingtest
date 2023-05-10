string = list(input())
n = len(string)

r = 0 #가로
c = 0 #세로

for i in range(1,n+1):
    if n % i == 0:
        if i <= n//i:
            r = i
            c = n//i

board = [[""] * r for _ in range(c)]

for i in range(c):
    for j in range(r):
        board[i][j] = string.pop(0)

ans = []

for i in range(r): #2
    for j in range(c): #3
        ans.append(board[j][i])

print("".join(map(str, ans)))