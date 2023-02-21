n = int(input())

num = list(map(int, input().split()))
primeNumber_count = 0

for i in num: # 리스트 num 의 모든 요소를 i로 받는다
    divisor_count = 0
    if i == 0:
        continue
    for j in range(2, i+1): 
        if i % j == 0:
            divisor_count += 1
    if divisor_count == 1:
        primeNumber_count += 1

print(primeNumber_count) 
             
