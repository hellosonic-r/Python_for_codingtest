###곱하기 혹은 더하기

nums = list(map(int,str(input())))

result = nums[0] # 0 

for i in range(1, len(nums)):
    if nums[i] <= 1 or result <=1:
        result += nums[i]
    else:
        result *= nums[i]

print(result)