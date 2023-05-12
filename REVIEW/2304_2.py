n = int(input())
p = []
for _ in range(n):
    loc, h = map(int, input().split()) #location: 왼쪽 면 위치 / h: 높이
    p.append((loc,h))

p.sort(key = lambda x:x[0])
max_h_idx = p.index(max(p, key = lambda x:x[1]))

start = p[0][1]
left_sum = 0
for i in range(1,max_h_idx+1): #1,2,3
    left_sum += (start*(p[i][0] - p[i-1][0]))
    if start < p[i][1]:
        start = p[i][1]

end = p[n-1][1]
right_sum = 0
for i in range(n-2,max_h_idx-1,-1): #5,4,3
    right_sum += (end*(p[i+1][0] - p[i][0]))
    if end < p[i][1]:
        end = p[i][1]

print(p[max_h_idx][1]+left_sum+right_sum)

