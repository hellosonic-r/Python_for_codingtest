answer = 0

def solution(n):
    
    def dfs(count, temp_list):
        global answer
        if sum(temp_list) >= n:
            if sum(temp_list) == n:
                answer += 1
            return
        for i in (1,2):
            dfs(count+1, temp_list+[i])
            
    dfs(0,[])
    ans = answer % 1234567
    
    return ans
