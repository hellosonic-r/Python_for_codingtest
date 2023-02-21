N = int(input())
a = 1
while True:
    a += 1
    if not N % a == 0:
        continue
    N /= a
    print(a)

#솔 실패.. 정답 참고
