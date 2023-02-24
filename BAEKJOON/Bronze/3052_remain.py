###나머지
nums = []
remain = []
for i in range(10):
    nums.append(int(input()))
    remain.append(nums[i] % 42)

print(len(list(set(remain))))
