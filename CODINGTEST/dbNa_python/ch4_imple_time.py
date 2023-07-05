##내풀이

n = int(input())

ans = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if 3 in list(map(int, str(i))) or 3 in list(map(int, str(j))) or 3 in list(map(int, str(k))):
                ans += 1

print(ans)

##교재풀이
n = int(input())

ans = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                ans += 1

print(ans)
