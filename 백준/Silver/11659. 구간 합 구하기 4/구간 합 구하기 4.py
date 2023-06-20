import sys

n, m = map(int, input().split())
num_list = list(map(int, sys.stdin.readline().split())) # 5 4 3 2 1

prefix_sum = [0 for _ in range(n+1)] 

for i in range(n): 
    prefix_sum[i+1] = prefix_sum[i] + num_list[i]

for _ in range(m):
    start, end = map(int, sys.stdin.readline().split())
    print(prefix_sum[end] - prefix_sum[start-1])

    