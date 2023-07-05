##시간초과 - 스택활용
def solution(people, limit):
    answer = 0
    people.sort()
    stack = []
    
    #[50, 50, 70, 80] # [40,40,200,200,200]
    
    v = []
    
    for i in range(len(people)): #0, 1,2,3,4.  -1,-2,-3,-4
        if i not in v:
            stack.append(people[i])
        
            for j in range(len(people)-1, i-1,-1):
                if i >= j:
                    stack.pop()
                    answer += 1
                    break
                    
                if j not in v:
                    if stack[-1] + people[j] <= limit:
                        answer += 1
                        stack.pop()
                        v.append(i)
                        v.append(j)
                        break
                       
    return answer



##다른코드 - 덱 활용
from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    people = deque(people)
    #50 70 80
    #50 50 70 80
    while people:
        if len(people) == 1:
            answer += 1
            break
        else:
            if people[0] + people[-1] <= limit:
                people.popleft()
                people.pop()
                answer += 1
            else:
                people.pop()
                answer += 1
        
    
    return answer
