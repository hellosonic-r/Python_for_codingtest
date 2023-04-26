###TC 10/15
# t = int(input())
# for test_case in range(1, t+1):
#     num, time = map(int, input().split())
#     num_list = list(map(int, str(num)))
#     ans = 0
#     count = 0
#     for i in range(len(num_list)):
#         if count == time:
#             break
#         else:
#             max_idx = len(num_list)-1
#             for j in range(len(num_list)-1, i, -1):
#                 if num_list[j] > num_list[max_idx]:
#                     max_idx = j
#                 else:
#                     continue
#         if num_list[i] < num_list[max_idx]:
#             num_list[i], num_list[max_idx] = num_list[max_idx], num_list[i]
#             count += 1
#     for i in range(len(num_list)):
#         ans += (num_list[i] * (10 ** (len(num_list)-1-i)))
#     print("#{} {}".format(test_case, ans))


##백트래킹, 가지치기(중복제거) 풀이
def dfs(count):
    global ans
    if count == k:
        ans = max(ans, int("".join(map(str, num_list))))
        return
    
    for i in range(len(num_list)-1):
        for j in range(i+1, len(num_list)):
            num_list[i],num_list[j] = num_list[j],num_list[i]
            check = int("".join(map(str,num_list)))
            if (count, check) not in v:
                dfs(count+1)
                v.append((count, check))
            num_list[i],num_list[j] = num_list[j],num_list[i]

t = int(input())

for test_case in range(1, t+1):
    num, k = map(int, input().split())
    num_list = list(map(int, str(num))) # [1,2,3]
    ans = -1
    v = []
    dfs(0)
    print("#{} {}".format(test_case, ans))


##다시 풀어보기
def dfs(count, prize):
    global ans
    if count == total: #교환횟수에 도달했다면
        #최대값 확인
        ans = max(ans, int("".join(map(str, prize))))
        return
    
    for i in range(len(num_list)-1): #먼저 숫자판 하나를 선택
        for j in range(i+1, len(num_list)): #남은 숫자판 중 하나를 선택
            num_list[i],num_list[j] = num_list[j],num_list[i] #선택한 숫자판 교환
            #중복 제거하기 위해(같은 dfs함수 내 82388과 82388은 동일할 경우 통과)
            #check 임시 변수 생성
            check = int("".join(map(str, num_list))) 
            #dfs함수 번호(count)와 숫자 정보(check)가 visited 리스트에 없다면
            if (count,check) not in visited:
                #visited에 dfs함수 번호(count)와 숫자 정보(check) 추가
                visited.append((count,check))
                #방문 체크 안되어있다면 다음 dfs함수 호출
                dfs(count+1, num_list)
            #다녀 와서는 바꿔놓은 숫자판 원상복귀
            num_list[i],num_list[j] = num_list[j],num_list[i]
            

t = int(input())
for test_case in range(1,t+1):
    num, total = map(int ,input().split())
    num_list = list(map(int,str(num)))
    visited = []
    ans = 0
    dfs(0,[])
    print("#{} {}".format(test_case, ans))