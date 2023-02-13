###최대공약수 6 8
# a, b = map(int, input().split())
# for i in range(min(a, b), 0, -1):
#     if a % i == 0 and b % i == 0:
#         print(i)
#         break # 6에서부터 1 까지의 범위에서 제일 큰 수가 들어가면 반복문 탈출



###최소공배수 6 8
# a, b = map(int, input().split())
# for i in range(max(a,b), (a*b)+1):
#     if i % a == 0 and i % b == 0:
#         print(i)
#         break



###문제풀이 ( 시간초과 )
# T = int(input())
# for i in range(T):
#     a, b = map(int, input().split())
#     for j in range(max(a, b), (a*b)+1):
#         if j % a == 0 and j % b == 0:
#             print(j)
#             break



###유클리드 호제법
# import math
# a, b = map(int, input().split())
# def gcd(a, b):
#     while b>0:
#         a , b = b , a % b
#     return a
# def lcm(a, b):
#     return a * b // gcd(a,b)
# print("최대공약수는 {} 이다".format(gcd(a,b)))
# print("최소공배수는 {} 이다".format(lcm(a,b)))



import math

T = int(input())

def gcd(a,b):
    while b>0:
        a, b = b, a%b
    return a
def lcm(a,b):
    return a*b // gcd(a,b)

for i in range(T):
    a , b = map(int, input().split())
    print(lcm(a,b))