n, m, l = map(int, input().split())
ball_visited = [0]*n
ball_visited[0] = 1

count = 0
i = 0
while True:
    if ball_visited[i%n] == m:
        break
    else:
        if ball_visited[i%n] % 2 == 1:
            ball_visited[(i+l)%n] += 1
            i = i + l
            count += 1
        elif ball_visited[i%n] % 2 == 0:
            ball_visited[-(-(i-l)%n)] += 1
            i = i - l
            count += 1
print(count)