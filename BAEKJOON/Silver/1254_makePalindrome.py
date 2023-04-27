s = list(input())
r_s = s[::-1]

if s == r_s:
    print(len(s))
else:
    min_ans = len(s)*2
    ans = len(s)*2
    for i in range(len(r_s)):
        #뒤집은 문자열을 하나하나 떼어서 붙여본다.
        check=s+r_s[i:len(r_s)]
        #만약 뒤집은 문자열이 오리지날과 일치한다면 팰린드롬이다.
        if check == check[::-1]:
            ans = len(check)
            if min_ans > ans:
                min_ans = ans
    print(min_ans)