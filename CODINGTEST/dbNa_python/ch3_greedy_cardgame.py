n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

result = []

for i in range(n):
    result.append(min(board[i]))

print(max(result))