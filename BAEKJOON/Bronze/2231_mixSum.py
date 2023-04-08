n=int(input())
# n 의 분해합은 각 자리수의 합
# m 의 분해합이 n인 경우 

n_list = list(map(int, str(n)))

ans = n
temp = 0
for i in range(n,0,-1):
    num_list = list(map(int, str(i)))
    if i + sum(num_list) == n:
        temp = i
        if temp < ans:
            ans = temp

if ans == n:
    print(0)
else:
    print(ans)