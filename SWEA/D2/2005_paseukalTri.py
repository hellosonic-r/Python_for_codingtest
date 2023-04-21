# def tri(i):
#     if i == n:
#         return
#     board[i].append(1)
#     for j in range(i-1):
#         board[i].append(board[i-1][j] + board[i-1][j+1])
#     board[i].append(1)
#     tri(i+1)
    
# t = int(input())

# for test_case in range(1,t+1):
#     n = int(input())
#     board = [[1]] + [[1,1]] + [[] for _ in range(n-2)]
#     tri(2)
    
#     for i in board:
#         print(i)
    
def tri(i):
    if i == n:
        return
    board[i].append(1)
    for j in range(i-1):
        board[i].append(board[i-1][j] + board[i-1][j+1])
    board[i].append(1)
    tri(i+1)
    

n,k = map(int, input().split())
board = [[1]] + [[1,1]] + [[] for _ in range(n-2)]
tri(2)
    
print(board[n-1][k-1])


    
