n = int(input())
board = []
for _ in range(n):
    x, y = map(int, input().split())
    board.append((x,y))

#x좌표가 증가하는 순으로. x좌표가 같으면 y좌표가 증가하는 순서로.
# -> y좌표 먼저 증가하는 순으로 정렬. x좌표 증가하는 순으로 정렬
board.sort(key = lambda x: x[1]) #먼저, y좌표가 증가하는 순으로 정렬
board.sort(key = lambda x: x[0]) #그 다음, x좌표가 증가하는 순으로 정렬

for i in board:
    print(" ".join(map(str, i)))
