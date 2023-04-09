import sys

n,m,l = map(int, sys.stdin.readline().split())

arr=[0]*n # 1 0 0 0 0 
arr[0] += 1
count = 0
ball_idx = 0 
while max(arr) < m:
    if arr[ball_idx] % 2 == 1:
        arr[(ball_idx+l)%n] += 1
        ball_idx = (ball_idx+l)%n
    elif arr[ball_idx] % 2 == 0:
        arr[(ball_idx-l+n)%n] += 1
        ball_idx = (ball_idx-l+n)%n
    count += 1
    
print(count)
