###1이될때까지(다른풀이)
##문제에서 n의 범위가 10만이 아닌 100억이었을 경우

n, k = map(int, input().split())
count = 0

while True:
    # n == k로 나누어떨어지는 수 가 될때까지 1씩 빼기 
    target = (n//k) * k
    count = count + (n-target)
    n = target
    if n < k:
        break
    #k로 나누기
    count = count + 1
    n=n//k

count = count + n - 1
print(count)