##Bfs -> 런타임에러
from collections import deque

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    v[y][x] = 1
    while queue:
        x,y = queue.popleft()
        if x*y == n:
            return v[y][x] - 1
        for i in range(2):
            nx = x+dx[i]
            ny = y + dy[i]
            queue.append((nx,ny))
            v[ny][nx] = v[y][x] + 1

t = int(input())
for test_case in range(1,t+1):
    n = int(input())
    v = [[0] * n for _ in range(n)]
    dx= [1,0]
    dy = [0,1]
    print(bfs(1,1))


##단순하게 풀기 - 임의의 최소값 비교 변수(ans) 활용하여 최솟값을 구하는 방식 
import math
t = int(input())
for test_case in range(1,t+1):
    n = int(input())
    total = []
    #n의 제곱근만큼만 확인해보면 된다.
    for i in range(1, int(math.sqrt(n)) +1):
        if n%i == 0:
            total.append((i, n//i)) #서로 곱했을 때 n이 나오는 두 숫자를 리스트에 저장한다.
    ans = 1000000e9
    for (x,y) in total: #리스트에 저장된 숫자들을 하나씩 꺼내본다.
        distance = x-1 + y-1 #(1,1)부터 (x,y)까지의 거리를 distance에 저장
        if ans > distance: #최솟값을 찾는다.
            ans = distance
    print("#{} {}".format(test_case, ans))

##좌표가 저장되어 있던 리스트에 거리정보를 저장하고, min() 메서드를 통해 최솟값을 구하는 방식
import math
t = int(input())
for test_case in range(1,t+1):
    n = int(input())
    total = []
    for i in range(1, int(math.sqrt(n)) +1):
        if n%i == 0:
            total.append((i, n//i))
    for i in range(len(total)): #1,1에서 시작
        distance = total[i][0]-1 + total[i][1]-1
        total[i] = distance
    print("#{} {}".format(test_case, min(total)))
