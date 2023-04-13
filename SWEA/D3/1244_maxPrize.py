###TC 10/15
# t = int(input())
# for test_case in range(1, t+1):
#     num, time = map(int, input().split())
#     num_list = list(map(int, str(num)))
#     ans = 0
#     count = 0
#     for i in range(len(num_list)):
#         if count == time:
#             break
#         else:
#             max_idx = len(num_list)-1
#             for j in range(len(num_list)-1, i, -1):
#                 if num_list[j] > num_list[max_idx]:
#                     max_idx = j
#                 else:
#                     continue
#         if num_list[i] < num_list[max_idx]:
#             num_list[i], num_list[max_idx] = num_list[max_idx], num_list[i]
#             count += 1
#     for i in range(len(num_list)):
#         ans += (num_list[i] * (10 ** (len(num_list)-1-i)))
#     print("#{} {}".format(test_case, ans))

def dfs(time):
    global ans, count
    if count == time:
        ans = max(ans, int("".join(map(str, num_list))))
        return
    
    for i in range(len(num_list)-1):
        for j in range(i+1, len(num_list)):
            num_list[i], num_list[j] = num_list[j], num_list[i]
            check = int("".join(map(str, num_list)))
            if (time, check) not in visited:
                dfs(time+1)
                visited.append((time, check))



t = int(input())

for test_case in range(1, t+1):
    ans = -1
    num, time = map(int, input().split())
    count = time
    num_list = list(map(int, str(num)))

    visited = []


    