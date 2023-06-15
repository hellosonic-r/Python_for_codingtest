def solution(s):
    str_list = s.split()
    arr = []
    for i in str_list:
        arr.append(int(i))
    
    answer = ''
    answer += str(min(arr))
    answer += " "
    answer += str(max(arr))
    return answer