##백트래킹 >> 실패
v = []

def solution(number, k):
    answer = ''
    num_list = list(map(int, str(number)))
    result = []
    
    def dfs(count, start, temp_list):
        if len(temp_list) == len(num_list) - k:
            result.append(int("".join(map(str, temp_list))))
            return
        if count == len(num_list) - k:
            return
        for i in range(start, len(num_list)):
            if i not in v:
                v.append(i)
                dfs(count+1, i+1, temp_list+[num_list[i]])
                v.pop()
            
    dfs(0,0,[])
    answer = str(max(result))
    
    return answer


#다른코드
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
