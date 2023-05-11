from collections import deque
import sys

queue = deque()

n = int(sys.stdin.readline())
for _ in range(n):
    command = sys.stdin.readline().strip()
    if command[:4] == "push":
        queue.append(int("".join(map(str,command[5:]))))
    elif command == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif command == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)
    elif command == "empty":
        if queue:
            print(0)
        else:
            print(1)
    elif command == "size":
        print(len(queue))
    elif command == "pop":
        if queue:
            print(queue.popleft())
        else:
            print(-1)
