# ##시간초과
# t = int(input())
# for test_case in range(1,t+1):
#     n = int(input())
#     a_list = list(map(int, input().split()))
#     total_a = []
#     ans = []
#     for _ in range(7):
#         a_list.append(a_list.pop(0))
#         if a_list[0] == 1:
#             i = 0
#             while True:
#                 n -= a_list[i%7]
#                 i+=1
#                 if n == 0:
#                     break
#             ans.append(i)
            
#     print("#{} {}".format(test_case, min(ans)))



##1인 인덱스 찾아서 그 인덱스를 시작점으로..
t = int(input())
for test_case in range(1,t+1):
    n = int(input())
    a_list = list(map(int, input().split()))

    firstIdx = [] #시작 인덱스를 저장하기 위한 리스트(1(수업있는날)인 값을 담는다)

    for i in range(len(a_list)):
        if a_list[i] == 1:
            firstIdx.append(i)
    
    answer = 1e9 #10억
    
    for idx in firstIdx: #시작 인덱스 
        classcnt = 0 #반복문 탈출을 위한 변수 #수업 있는날이면 1씩 증가시켜주면됨
        day_cnt = 0 #날짜 카운트 #시작인덱스가 0이 아니어도 (시작 인덱스와 관계없이) 날짜를 0으로 초기화
        while classcnt<n:
            if a_list[idx%7] == 1: #수업들을 수 있는날
                classcnt+=1 #수업 들었다고 표시
            idx += 1 #다음날
            day_cnt += 1 #날짜 카운트
        answer = min(answer, day_cnt)
        
    print("#{} {}".format(test_case, answer))



## 다시풀기
t = int(input())

for test_case in range(1,t+1):
    n = int(input())
    num_list = list(map(int, input().split()))

    start_idx = []
    
    #수업이 있는 요일(인덱스)를 모두 찾는 for문
    for i in range(len(num_list)):
        if num_list[i] == 1:
            start_idx.append(i)
            
    ans = [] 
    #수업이 있는 요일을 꺼내서 그 요일이 카운트의 시작점이 된다.
    for idx in start_idx:
        cnt = 0 #수업을 들은 횟수 
        days = 0 #총 며칠이 지났는지 카운트 
        while True:
            if cnt == n: #만약 수업을 다 듣는다면, 반복문 탈출
                break
            if num_list[idx%7] == 1: #수업이 있는날이면
                cnt += 1 #수업을 들은 횟수 += 1 
            idx += 1 #요일 += 1
            days += 1 #총 며칠 지났는지 카운트 += 1
        ans.append(days)

    print("#{} {}".format(test_case, min(ans)))



