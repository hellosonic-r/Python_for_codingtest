n = int(input())
meet = []
for _ in range(n):
    meet.append(list(map(int, input().split())))

meet.sort(key = lambda x:x[0])
meet.sort(key = lambda x:x[1])

start = meet[0][0]
end = meet[0][1]
cnt = 1
for i in range(1, len(meet)):
    if meet[i][0] >= end:
        start = meet[i][0]
        end = meet[i][1]
        cnt += 1

print(cnt)
    
