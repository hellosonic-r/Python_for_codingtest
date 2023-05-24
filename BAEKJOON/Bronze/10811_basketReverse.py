n, m = map(int, input().split())
num_list = list(range(1,n+1))
for _ in range(m):
    start, end = map(int, input().split())
    i  = start - 1
    j = end - 1
    first = num_list[:i]
    middle = num_list[i:j+1]
    last = num_list[j+1:]
    num_list = first + middle[::-1] + last

print(" ".join(map(str, num_list)))


