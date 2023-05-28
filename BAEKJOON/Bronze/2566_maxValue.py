board = [list(map(int, input().split())) for _ in range(9)]

max_val = -1
y = -1
x = -1
for i in range(9):
    for j in range(9):
        if max_val < board[i][j]:
            max_val = board[i][j]
            y = i+1
            x = j+1

print(max_val)
print(y, x)
