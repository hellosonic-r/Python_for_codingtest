N = int(input())
i = 2 #나누는 수가 2부터 시작

while N != 1: #N이 1이 아니면 계속 반복문 실행
    if N % i == 0: #N이 i로 나누어떨어지면
        print(i) #i출력
        N /= i
    else:
        i += 1

