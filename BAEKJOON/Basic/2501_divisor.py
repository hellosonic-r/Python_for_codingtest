#약수구하기
import sys

n, k= map(int, sys.stdin.readline().split())

d_list = []
d = 1

for i in range(n): # 6 - 1, 2, 3, 4,  5  6 # 25 - 1, 5, 25 
    if n % d == 0:
        d_list.append(d)
        d += 1
    else:
        d +=1 

print(0 if k > len(d_list) else d_list[k-1])

