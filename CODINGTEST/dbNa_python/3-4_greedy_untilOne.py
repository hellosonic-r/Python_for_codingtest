###1이 될때까지
#n에서 1을 뺀다
#n을 k 로 나눈다

n, k = map(int, input().split()) #14,4 1을 두번 수행 n = 12 / 2를 한번 수행 n =3 / 1을 두번 수행
count = 0

while n != 1: # 14
    if n % k != 0: 
        n -= 1
        count += 1
    elif n % k == 0: 
        n /= k 
        count += 1

print(count)

