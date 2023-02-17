#n까지의 합
def sol(n):
    if n == 0: #정지할 조건
        return 0
    else:
        return n + sol(n-1)
print(sol(10)) # 55

#구구단
def solution(a, b):
    if b == 9:
        print(a, "x",b,"=",a*b)
        return 
    else:
        print(a,"*",b,"=",a*b)
        return solution(a, b+1)
print(solution(3,1))

#배열의합
# def arr_sum(arr, i):
#     if i == len(arr) - 1:
#         return arr[i]
#     else: 

# 1, 2, 2, 3, 3, 3, 4, 4, 4, 4,,, 의 합
a, b = map(int, input().split())

def repeatSum(x,y):
    if x > y: 
        return 0
    else:
        return x*x + repeatSum(x+1, y)

print(repeatSum(a, b))
