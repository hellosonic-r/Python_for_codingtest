def solution(number, k):
    answer = ''
    stack = []
    for i in number:
        #작은 수가 제거되었는지 확인
        while stack and k>0 and stack[-1] < i:
            stack.pop()
            k-=1
        stack.append(i)
        
    answer = "".join(map(str, stack[:len(number)-k]))
    return answer