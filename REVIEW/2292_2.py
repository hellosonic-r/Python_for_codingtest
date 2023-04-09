n = int(input())

ans = 1
time = 1
while True:
    if n <= ans:
        break
    else:
        ans = ans + 6*time
        time += 1
    
if n == 1:
    print(1)
else:
    print(time)