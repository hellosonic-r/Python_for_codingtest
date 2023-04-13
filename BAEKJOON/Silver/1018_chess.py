n, m = int(input().split())

chess = []
for i in range(n):
    chess.append(list(map(str, input())))

def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    if chess[x][y] == "W":
        chess[x-1][y] =="B"
        chess