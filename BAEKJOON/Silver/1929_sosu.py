###소수 구하기 
##시간초과
import sys
m, n = map(int, sys.stdin.readline().split())

nums = list(range(m,n+1))


for num in nums:
    count = 0
    for i in range(1,(num//2)+1):
        if num % i == 0:
            count+=1
    if count == 1:
        print(num)


##에라토스테네스의 체

