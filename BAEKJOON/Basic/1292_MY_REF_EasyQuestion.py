
import sys

a, b = map(int, sys.stdin.readline().split())

num_list = []
for i in range(1, b+1): # a = b 같으면 에러가 발생하므로 b >> b+1 로 변경
    for j in range(1,i+1):  
        num_list.append(i)

fin = 0
for k in range(a-1, b):
    fin = fin + num_list[k]

print(fin)

## 런타임에러

