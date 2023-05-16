n, k = map(int, input().split())
num_list = []
for _ in range(n):
    num_list.append(int(input()))

num_list.sort(reverse=True)
cnt = 0
for i in range(n):
    if k >= num_list[i]:
        cnt += (k // num_list[i])
        k = k % num_list[i]
    if k == 0:
        break

print(cnt)

