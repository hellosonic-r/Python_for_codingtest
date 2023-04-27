##시간초과
n = int(input())
ans = []
for _ in range(n):
    name, command = map(str, input().split())
    if command == 'enter':
        ans.append(name)
    elif command == 'leave':
        ans.remove(name)

ans.sort(reverse=True)

for i in ans:
    print(i)

##딕셔너리로 시간복잡도 해결
import sys

n = int(sys.stdin.readline())
dic = {}

for _ in range(n):
    name, command = map(str, sys.stdin.readline().split())
    dic[name] = command #딕셔너리에 key:name value:command 를 저장
    if command == "leave": #만약 value가 leave 라면
        del dic[name] #del dic[key]를 이용해 키를 제거

d = sorted(dic.items(), reverse = True) 
dic = dict(d)

for key in dic.keys():
    print(key)
