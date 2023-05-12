n = int(input())
num_list = list(map(int, input().split()))
bcnt = 1
max_bcnt = 1
scnt = 1
max_scnt = 1
for i in range(1,n):
    if num_list[i] >= num_list[i-1]:
        bcnt += 1
        if max_bcnt < bcnt:
            max_bcnt = bcnt
    else:
        bcnt = 1
    if num_list[i] <= num_list[i-1]:
        scnt += 1
        if max_scnt < scnt:
            max_scnt = scnt
    else:
        scnt = 1
print(max(max_bcnt, max_scnt))

