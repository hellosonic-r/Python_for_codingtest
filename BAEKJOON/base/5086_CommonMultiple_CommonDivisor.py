import sys

a=1 #변수 선언/초기화
b=1

while a > 0 and b > 0: #while 에 변수 쓰려면 앞에 선언 및 초기화가 되어있어야 한다
    a,b = map(int, sys.stdin.readline().split())
    if a == 0 and b == 0:
        break
    elif b % a == 0:
        print("factor")
    elif a % b == 0:
        print("multiple")
    else: 
        print("neither")
