###벌집
##메모리 초과
# n = int(input())
# honeycomb_list = []
# num = 1
# count = 1
# x = 1
# while num != n:
#     honeycomb = []
#     for i in range(6*x):
#         num += 1
#         honeycomb.append(num)
#         if num == n:
#             break
#     x += 1
#     honeycomb_list.append(honeycomb)
#     count += 1

# print(count)


##시간초과 (pypy로 해결 성공 코드 확인)
# n = int(input())
# num = 1
# count = 1
# x = 1
# while num != n:
#     for i in range(6*x):
#         num += 1
#         if num == n:
#             break
#     x += 1
#     count += 1

# print(count)


##다른사람 풀이
n = int(input())
num = 1
count = 1
while n > num:
    num = num + 6 * count
    count += 1
print(count)