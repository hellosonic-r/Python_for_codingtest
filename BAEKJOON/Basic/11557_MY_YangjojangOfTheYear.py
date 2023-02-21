###Try1
# import sys

# t = int(input()) #테스트케이스 수

# for i in range(t):
#     n = int(input()) #학교 수
#     s_list = []
#     l_list = []
#     l_high = 0
#     for j in range(n):
#         s, l = input().split()
#         s_list.append(s)
#         l_list.append(l)
#     l_high = max(l_list)
#     print(l_list.index(l_high))    



###Try2
t = int(input()) #테스트 케이스 수

for i in range(t):
    n = int(input()) #학교 수
    s_list = []
    l_list = []
    for j in range(n):
        s, l = input().split()
        s_list.append(s)
        l_list.append(l)
        m = 0
        for k in range(len(l_list)): #l_list의 인덱스 찾기
            while True:
                if k == len(l_list) - 1:
                    break
                elif int(l_list[k]) > int(l_list[k+1]):
                    m = k
                else:
                    continue
    print(s_list[m])

                
###솔 실패...