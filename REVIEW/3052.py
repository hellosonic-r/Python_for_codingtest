nums = []
for _ in range(10):
    nums.append(int(input()))

d = []
for num in nums:
    d.append(num%42)

print(len(list(set(d))))