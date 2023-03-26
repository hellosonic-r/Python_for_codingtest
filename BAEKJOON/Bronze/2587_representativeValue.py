import math
num_li = []
for _ in range(5):
    num_li.append(int(input()))
num_li.sort()

print(math.trunc(sum(num_li)/5),num_li[2],sep="\n")