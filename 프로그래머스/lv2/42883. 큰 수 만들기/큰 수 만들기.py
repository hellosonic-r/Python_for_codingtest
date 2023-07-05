def solution(number, k):
    answer = ''
    stack = []
    for i in number:
        while stack and k>0 and i>stack[-1]:
            stack.pop()
            k-=1
        stack.append(i)
    answer = "".join(map(str, stack[:len(number)-k]))
            
    return answer