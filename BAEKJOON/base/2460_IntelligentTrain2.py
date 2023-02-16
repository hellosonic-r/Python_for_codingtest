import sys

count_list = []
count = 0
out_man_list, in_man_list = [], []
for i in range(10):
    out_man, in_man = list(map(int, sys.stdin.readline().split()))
    out_man_list.append(out_man)
    in_man_list.append(in_man)
    count = count + in_man_list[i] - out_man_list[i]
    count_list.append(count)

print(max(count_list))


#ref
'''
train = [[*map(int, input().split())] for _ in range(1, 11)]
l = [0] * 11
l[1] = train[0][1]

for i in range(2, 11):
    l[i] = l[i - 1] - train[i - 1][0] + train[i - 1][1]

print(max(l))
'''
