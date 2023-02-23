n, m = map(int, input().split())

nums = list(map(int, input().split()))


sums_list = []
for i in range(len(nums)):
    sums = 0
    for j in range(len(nums)):
        if nums[j] == nums[i]:
            continue
       
        for k in range(len(nums)):
            if nums[k] == nums[j] or nums[k] == nums[i]:
                continue
            else:
                sums = nums[i] + nums[j] + nums[k]
                if sums <= m:
                    sums_list.append(sums)
                else:
                    continue
print(max(sums_list))

# final = sorted(list(set(sums_list)))
# idx = 0
# while True:
#     if final[idx] > m:
#         break
#     idx += 1

# if idx == 0:
#     idx == 1
# print(final[idx-1])
