from collections import deque
n, k = map(int, input().split())

queue = deque(range(1,n+1))
ans = []

while queue:
    for i in range(k-1):
        queue.append(queue.popleft())
    ans.append(queue.popleft())
    
print(str(ans).replace("[","<").replace("]",">"))


# string = "Hello world"
# l = string.replace("Hello","Hi").replace("world","Mino")
# print(l)