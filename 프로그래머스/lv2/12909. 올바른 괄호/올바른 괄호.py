def solution(s):
    answer = True
    
    stack = []
    for i in s:
        if i == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(i)
                
        else:
            stack.append(i)
            
    if stack:
        answer = False
    else:
        answer = True
        
    return answer


#