# #왜 틀리지
string = list(input())
search = list(input())
ans = 0
i = 0
mini_cnt = 0
while string:
    x = string.pop(0)
    if x == search[i]:
        mini_cnt += 1
        i = (i+1)%len(search)
    else:
        if x == search[0]:
            i = 1
            mini_cnt = 1
        else:
            i = 0
            mini_cnt = 0

    if mini_cnt == len(search):
        ans += 1
        mini_cnt = 0

print(ans)


##다른 코드
a = list(input())
b = list(input())

cnt = 0
n = 0

while n <= len(a)-len(b):
    if a[n:n+len(b)] == b:
        cnt += 1
        n += len(b)
    else:
        n += 1

print(cnt)

