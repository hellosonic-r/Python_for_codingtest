# ##내풀이
# n, k = map(int, input().split()) #n에서 1을 뺀다. n을 k로 나눈다.
# result = []

# cnt = 0 
# while True:
#     if n == 1:
#         break
#     if n % k == 0:
#         n = n // k
#         cnt += 1
#     else:
#         n -= 1
#         cnt += 1

# print(cnt)


# ##교재 풀이1
# n, k = map(int, input().split())
# result = 0

# while n >= k:
#     while n % k != 0:
#         n -= 1
#         result += 1
#     n = n // k
#     result += 1

# while n > 1:
#     n -= 1
#     result += 1

# print(result)





