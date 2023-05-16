n, k = map(int, input().split()) 
coin_types = []
for i in range(n):
    coin_types.append(int(input()))

coin_types.sort(reverse = True)
#[50000, 10000, 5000, 1000, 500, 100, 50, 10, 5, 1]
count = 0
for j in range(n): # k = 4200 일때
    if k // coin_types[j] >= 1:
        count = count + k // coin_types[j]
        k = k % coin_types[j]
    else:
        continue

print(count)


##다시 풀기
n, k = map(int, input().split())
num_list = []
for _ in range(n):
    num_list.append(int(input()))

num_list.sort(reverse=True)
cnt = 0
for i in range(n):
    if k >= num_list[i]: #같다 주의
        cnt += (k // num_list[i])
        k = k % num_list[i]
    if k == 0:
        break

print(cnt)



