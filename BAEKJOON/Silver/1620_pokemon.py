##시간초과
import sys

n, m = map(int, input().split())
lst = []
for _ in range(n):
    lst.append(sys.stdin.readline())

for _ in range(m):
    x = sys.stdin.readline()
    if 65<=ord(x[0])<=90 or 97<=ord(x[0])<=122:
        print(lst.index(x)+1)
    else:
        print(lst[int(x)-1])


##시간초과
import sys

n, m = map(int, input().split())
d = {}
for i in range(1, n+1):
    d[i] = sys.stdin.readline().rstrip()

for _ in range(m):
    x = sys.stdin.readline()
    if 65<=ord(x[0])<=90 or 97<=ord(x[0])<=122: #영어이면
        for j in d.keys():
            if d[j] == x:
                print(j)
    else:
        print(d[int(x)])


##딕셔너리 두 개 만들기
import sys

n, m = map(int, input().split())
d_alpha = {} #알파벳을 값으로
d_num = {} #숫자를 값으로

for i in range(1, n+1):
    x = sys.stdin.readline().rstrip()
    d_alpha[i] = x
    d_num[x] = i

for j in range(m):
    y = sys.stdin.readline().rstrip()
    if 65<=ord(y[0])<=90 or 97<=ord(y[0])<=122: #영어이면
        print(d_num[y])
    else:
        print(d_alpha[int(y)])


##다른 풀이: 딕셔너리 하나로
import sys

n,m = map(int, input().split())
d = {}

for i in range(1, n+1):
    name = sys.stdin.readline().rstrip()
    d[name] = str(i)
    d[str(i)] = name

for i in range(m):
    x = input().rstrip()
    print(d[x])