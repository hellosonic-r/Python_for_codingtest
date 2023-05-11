n = int(input()) #정확히 n킬로그램

cnt = 0
while True:
    if n % 5 == 0:
        cnt += (n // 5)
        n = 0
    else:
        n = n-3
        cnt += 1
    if n <= 0:
        break
    
if n == 0:
    print(cnt)
else:
    print(-1)