t = int(input())
for test_case in range(1,t+1):
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))

    if len(a_list) > len(b_list):
        s_list = b_list
        l_list = a_list
    else:
        s_list = a_list
        l_list = b_list

    max_ans = 0
    for i in range(len(l_list)-len(s_list)+1):
        ans = 0
        for j in range(len(s_list)):
            ans += (s_list[j] * l_list[j+i])
        if max_ans < ans:
            max_ans = ans
    
    print("#{} {}".format(test_case, max_ans))

