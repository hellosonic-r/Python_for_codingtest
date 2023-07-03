##내 풀이
n, m, k = map(int, input().split()) #배열의 크기 n, 숫자 더해지는 횟수 m, k

num_list = list(map(int, input().split())) # 2,4,5,4,6
result = []
cnt = 0
while True:
    if len(result) == m:
        break
    temp = 0
    if cnt < k:
        idx = 0
        for i in range(len(num_list)):
            if temp < num_list[i]:
                temp = num_list[i]
                idx = i
        cnt += 1
    else:
        for i in range(len(num_list)):
            if i != idx:
                if temp < num_list[i]:
                    temp = num_list[i]
        cnt = 0

    result.append(temp)

print(result)


##교재 풀이1
n, m, k = map(int, input().split())
num_list = list(map(int, input().split()))

num_list.sort()

first = num_list[-1]
second = num_list[-2]

ans = 0

while True:
    for i in range(k):
        if m == 0:
            break
        ans += first
        m -= 1
    if m == 0:
        break
    ans += second
    m -= 1

print(ans)


##교재 풀이2 - m의 크기가 클 때 >> 수학적 계산
n, m, k = map(int, input().split())
num_list = list(map(int, input().split()))

num_list.sort()

ans = 0

first = num_list[-1]
second = num_list[-2]

cnt = (m // (k+1)) * k + (m % (k+1))

ans = first * cnt + second *(m-cnt)

print(ans)