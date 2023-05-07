t = int(input())
for test_case in range(1,t+1):
    n = int(input())
    num_list = list(map(int ,input().split()))
    max_ans = -1 #단조 증가하는 수가 아니면 -1이 출력될 것이다.
    #두 개의 숫자를 뽑는 2중 for문
    for i in range(n-1):
        for j in range(i+1, n):
            check = num_list[i] * num_list[j] #우선 곱해본다.
            check_list = list(map(int, str(check)))
            danzo = 1 #단조 = 1
            for k in range(len(check_list)-1): 
                if check_list[k] > check_list[k+1]: #만약 다음 숫자보다, 현재 숫자가 더 크다면
                    danzo = 0 #단조 증가하는 수가 아니다.
                    break
            if danzo == 1: #단조일 때, 최대값을 찾는다.
                if max_ans < check: 
                    max_ans = check
    print(max_ans)
                
