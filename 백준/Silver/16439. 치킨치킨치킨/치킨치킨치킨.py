n, m = map(int, input().split())

board = []

for _ in range(n):
    board.append(list(map(int, input().split())))

answer = 0

for i in range(m-2):
    for j in range(i+1, m-1):
        for k in range(j+1, m):
            temp_sum = 0
            for z in range(len(board)):
                temp_sum += max(board[z][i],board[z][j],board[z][k])
            if answer < temp_sum:
                answer = temp_sum

print(answer) 

