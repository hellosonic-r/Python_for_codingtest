n = int(input())
num_list = list(map(int, input().split()))
ans = 0
for i in range(len(num_list)):
    if num_list[i] == 1:
        continue
    cnt = 0
    for j in range(2,num_list[i]+1):
        if num_list[i] % j ==0:
            cnt += 1
        if cnt>=2:
            break
    if cnt == 1:
        ans += 1

print(ans)