n = int(input())
num_list = list(map(int, input().split()))

num_list.sort()

ans = 0
temp_time = 0
for i in range(len(num_list)):
    temp_time += num_list[i]
    ans += temp_time

print(ans)