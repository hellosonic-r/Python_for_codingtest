# def fibo(n):
#     if n == 0:
#         return 0
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fibo(n-1) + fibo(n-2)

# n = int(input())
# print(fibo(n))

n = int(input())
num = [0,1]
for i in range(2,n+1):
    num.append(num[i-1] + num[i-2])

print(num[-1])