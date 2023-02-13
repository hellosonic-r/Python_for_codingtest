import sys

x_nums = []
y_nums = []

for i in range(3):
    x, y = map(int, sys.stdin.readline().split())
    x_nums.append(x)
    y_nums.append(y)

for j in range(len(x_nums)):
    if x_nums.count(x_nums[j]) == 1:
        x4 = x_nums[j]
    if y_nums.count(y_nums[j]) == 1:
        y4 = y_nums[j]

print(x4,y4)