t = int(input())
for test_case in range(1, t+1):
    n, k = map(int,input().split())
    score_list = []
    for _ in range(n):
        mid, end, hw = map(int, input().split())
        score_list.append(mid * (0.35) + end * (0.45) + hw * (0.2))
        
    k_score = score_list[k-1]
    sorted_score = sorted(score_list, reverse=True)
    
    ans_num = 0
    for i in range(len(sorted_score)):
        if sorted_score[i] == k_score:
            ans_num = i+1
            
    result = ""
    check = ans_num / n
    if check <= 0.1:
        result = "A+"
    elif check <= 0.2:
        result = "A0"
    elif check <= 0.3:
        result = "A-"
    elif check <= 0.4:
        result = "B+"
    elif check <= 0.5:
        result = "B0"
    elif check <= 0.6:
        result = "B-"
    elif check <= 0.7:
        result = "C+"
    elif check <= 0.8:
        result = "C0"
    elif check <= 0.9:
        result = "C-"
    else:
        result = "D0"
    print("#{} {}".format(test_case, result))
        
            
            
               