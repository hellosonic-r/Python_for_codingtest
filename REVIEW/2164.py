###카드2
from collections import deque

n = int(input())
card = []
for i in range(1,n+1):
    card.append(i)
queue = deque(card)

while len(queue) != 1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue[0])

