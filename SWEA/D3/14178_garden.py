##TC 10000개 중 6400 통과
# t = int(input())
# for test_case in range(1,t+1):
#     n, d = map(int, input().split())
#     num = d+1
#     cnt = 1
#     while num  <= n:
#         num+=(2*d+1)
#         cnt+=1
#     if n-num > d+1:
#         cnt += 1
#         print("#{} {}".format(test_case,cnt))
#     else:
#         print("#{} {}".format(test_case,cnt))

##Pass 코드
t = int(input())
for test_case in range(1,t+1):
    n, d = map(int, input().split())
    num = 1
    cnt = 0
    while num  <= n:
        num+=(2*d+1)
        cnt+=1
    print("#{} {}".format(test_case,cnt))
        