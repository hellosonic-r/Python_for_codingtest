###어떤 수 a의 약수 (중복제거) 를 리스트에 넣는 코드
# a = int(input())
# arr = []
# x = 2
# while a != 1:
#     if a % x == 0:
#         print(x)
#         arr.append(x)
#         a /= x 
#     else :
#         x += 1
# print(list(set(arr)))

###테스트 케이스 입력 없이
# a, b = map(int, input().split())

# a_list = []
# b_list = []
# x = 2
# y = 2

# while a != 1:
#     if a % x == 0:
#         a_list.append(x)
#         a /= x
#     else:
#         x += 1
# print(list(set(a_list)))

# while b != 1:
#     if b % y == 0:
#         b_list.append(y)
#         b /= y
#     else :
#         y += 1
# print(list(set(b_list)))

# ab_list = []
# ab_list = list(set(list(set(a_list)) + list(set(b_list))))
# print(ab_list)

# fin = 1
# for j in range(len(ab_list)):
#     fin = fin * ab_list[j]
# print(fin)


###Try1
# T = int(input())
# a_list = []
# b_list = []
# x = 2
# y = 2
# fin = 1
# for i in range(T):
#     a, b = map(int, input().split())
#     if a * b == a or a * b == b:
#         print(max(a,b))
#     else :
#         while a != 1:
#             if a % x == 0:
#                 a_list.append(x)
#                 a /= x
#             else:
#                 x += 1
#         while b != 1:
#             if b % y == 0:
#                 b_list.append(y)
#                 b /= y
#             else :
#                 y += 1
#         ab_list = []
#         ab_list = list(set(list(set(a_list)) + list(set(b_list))))
#         for j in range(len(ab_list)):
#             fin = fin * ab_list[j]
#         print(fin)


#Try2
import math

T = int(input())
for i in range(T):
    a, b = map(int, input().split())

    a_list = []
    b_list = []
    x = 2
    y = 2
    if a % b == 0 or b % a == 0:
        print(int(max(a,b)))
    else:
        while a != 1:
            if a % x == 0:
                a_list.append(x)
                a /= x
            else:
                x += 1
    
        while b != 1:
            if b % y == 0:
                b_list.append(y)
                b /= y
            else :
                y += 1
    
        ab_list = []
        ab_list = list(set(list(set(a_list)) + list(set(b_list))))
    
        fin = 1
        for j in range(len(ab_list)):
            fin = fin * ab_list[j]
        print(fin)

#솔 실패.. 많이 배웠다