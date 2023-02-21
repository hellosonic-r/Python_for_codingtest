###왜 솔 실패?
'''
import sys

n = int(input())

num = list(map(int, sys.stdin.readline().split()))

fin_list = [] # 2 3 5 7
for i in range(len(num)):
    if num[i] == 2:
        fin_list.append(num[i])
    else:
        for j in range(num[i]):
            if j <= 1:
                continue
            elif num[i] % j == 0:
                break
            else:
                fin_list.append(num[i])

print(len(list(set(fin_list))))
'''
### 솔 실패 이해 완료 반례 1 \n 9


## 성공 코드
import sys

n = int(input())

num_list = list(map(int, sys.stdin.readline().split())) # 2 5 7 9
fin_list = []
for num in num_list: # 리스트 안의 요소를 하나씩
    count = 0
    if num <= 1:
        continue
    else:
        for divisor in range(2, num+1):
            if num % divisor == 0:
                count += 1
    if count == 1:
        fin_list.append(num)
print(len(fin_list))

        