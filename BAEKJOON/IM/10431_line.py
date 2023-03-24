##실패코드
# p = int(input())
# test_case = []
# for i in range(p):
#     test_case.append(list(map(int, input().split())))
    
# #   [[1 900 901 902 903 904 905 906 907 908 909 910 911 912 913 914 915 916 917 918 919],
# #    [2 919 918 917 916 915 914 913 912 911 910 909 908 907 906 905 904 903 902 901 900]]
# cnt = [0] * p
# for i in range(p): # 0 1 2 3 
#     temp = test_case[i]
#     temp.pop(0)
#     for j in range(len(temp)):
#         for k in range(j+1,len(temp)):
#             if temp[j] > temp[k]:
#                 temp.insert(1, temp[k])
#                 temp.pop(k+1)
#                 cnt[i] += k - j
#             else:
#                 continue

# for z in range(p):
#     print(z+1, cnt[z],sep = " ")


# n = int(input())

# for _ in range(n):
#     num_list = list(map(int, input().split()))
#     test_case = num_list[0]
#     cnt = 0
#     for i in range(1, len(num_list)):
#         if i == 1:
#             continue
#         else:
#             for j in range(i,0,-1):
#                 if num_list[j] < num_list[j-1]:
#                     num_list[j-1], num_list[j] = num_list[j], num_list[j-1]
#                     cnt += 1
#     print(test_case,cnt)

# n = int(input())

# for _ in range(n):
#     num_list = list(map(int, input().split()))
#     test_case = num_list[0]
#     cnt = 0
#     for i in range(1, len(num_list)):
#         if i == 1:
#             continue
#         else:
#             for j in range(i-1,0,-1):
#                 if num_list[i] < num_list[j]:
#                     num_list[j], num_list[i] = num_list[i], num_list[j]
#                     cnt += 1
#     print(test_case,cnt)




## 성공코드

# n = int(input())

# for _ in range(n):
#     num_list = list(map(int, input().split()))
#     test_case = num_list[0]
#     cnt = 0
#     for i in range(1, len(num_list)-1):
#         for j in range(i+1,len(num_list)): #뒤에 있는 숫자들 비교
#             if num_list[i] > num_list[j]:
#                 num_list[i],num_list[j] = num_list[j],num_list[i]
#                 cnt += 1
#     print(test_case, cnt)


n = int(input())

for _ in range(n):
    num_list = list(map(int, input().split()))
    test_case = num_list[0]
    cnt = 0
    #맨 뒤의 인덱스의 값과
    for i in range(len(num_list)-1, 0, -1):
        #맨 뒤의 바로 앞 인덱스부터 제일 앞 인덱스까지 값 비교 
        for j in range(i-1,0,-1):
            if num_list[i] < num_list[j]:
                num_list[i], num_list[j] = num_list[j], num_list[i]
                cnt += 1
    print(test_case,cnt)
    

        

