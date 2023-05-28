n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

board.sort(key = lambda x:x[0])
board.sort(key = lambda x:x[1])

for i in board:
    print(" ".join(map(str, i)))