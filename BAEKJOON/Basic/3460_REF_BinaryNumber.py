#이진수 함수를 이용한 문제풀이

t = int(input())

for _ in range(t):
    n = bin(int(input()))[2:]
    for i in range(len(n)+1):
        if i == len(n):
            print()
        else:
            if n[-i-1] == "1":
                print(i, end = " ")
            else: 
                continue
