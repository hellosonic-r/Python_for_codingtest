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