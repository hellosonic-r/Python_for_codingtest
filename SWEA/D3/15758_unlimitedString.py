test = int(input())
for test_case in range(1, test+1):
    s, t = map(str, input().split())
    ans = ""
    s_len = len(list(s)) #문자열 s의 길이
    t_len = len(list(t)) #문자열 t의 길이
    #문자열 s와 문자열 t의 길이가 서로 같을 때
    if len(list(s)) == len(list(t)): 
        #문자열 s가 문자열 t와 같다면 ans에 yes 저장
        if s == t:
            ans = "yes"
        #문자열 s가 문자열 t와 다르다면 ans에 no 저장
        else:
            ans = "no"
    #입력받은 두 문자열의 길이가 같다면, 두 문자열 길이의 최소공배수가 될 때까지 문자열을 반복하고, 
    #반복한 문자열이 같으면 yes 다르면 no를 ans에 저장하는 코드 작성
    else:
        temp_s = s #변하지 않는 임시 값 
        temp_t = t
        while len(list(s)) < t_len * s_len:
            s = s + temp_s
        while len(list(t)) < s_len * t_len:
            t = t + temp_t
        if s == t:
            ans = "yes"
        else:
            ans = "no"
    print("#{} {}".format(test_case, ans))