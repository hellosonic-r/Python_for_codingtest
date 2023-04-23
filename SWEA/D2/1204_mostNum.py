t = int(input())
for test_case in range(1, t+1):
    test_num = int(input())
    score_list = list(map(int, input().split()))
    result_list = [0]*101
    for i in range(101):
        result_list[i] = score_list.count(i)
    max_result = 0
    ans_idx = -1
    for j in range(len(result_list)): # 0~ 100
        if max_result <= result_list[j]:
            max_result = result_list[j]
            ans_idx = j

    print("#{} {}".format(test_num, ans_idx))
        

t = int(input())

for test_case in range(1, t+1):
    score_list = [0] * 101
    n = int(input())
    num_list = list(map(int, input().split()))
    for i in range(101):
        score_list[i] += num_list.count(i)
    
    result = -1
    ans = -1
    
    for i in range(len(score_list)):
        if score_list[i] >= result:
            result = score_list[i]
            ans = i
        
    print("#{} {}".format(test_case, ans))

