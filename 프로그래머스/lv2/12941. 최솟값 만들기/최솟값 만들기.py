def solution(A,B):
    answer = 0
    
    A.sort()
    B.sort(reverse=True)
    length = len(A) #3
    for i in range(length): #0,1,2
        answer += (A[i]*B[i])
        

    return answer