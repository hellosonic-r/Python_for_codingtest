##내 풀이
board = []
length = 0
for i in range(5):
    board.append(list(input()))
    if length < len(board[i]):
        length = len(board[i]) 

for i in range(5):
    if len(board[i]) != length:
        for j in range(length - len(board[i])):
            board[i].append("")

ans = ""
for i in range(length):
    for j in range(5):
        ans += board[j][i]

print(ans)


##다른 풀이
board = []
length = 0
for i in range(5):
    board.append(list(input()))
    if length < len(board[i]):
        length = len(board[i])

ans = ""
for i in range(length):
    for j in range(5):
        if i < len(board[j]):
            ans += board[j][i]

print(ans)
    