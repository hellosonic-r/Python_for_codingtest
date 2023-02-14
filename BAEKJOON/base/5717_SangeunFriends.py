import sys

while True:
    a, b = map(int, sys.stdin.readline().split())
    if a == 0 and b == 0: # a, b를 0을 입력하면
        break             # 반복문 탈출
    print(a+b)