def solution(brown, yellow):
    answer = []
    yellow_list = []
    for i in range(1, yellow+1):
        temp = [0,0]
        if yellow%i == 0:
            temp[0] = yellow//i
            temp[1] = i
            temp.sort()
            if temp not in yellow_list:
                yellow_list.append(temp)
            else:
                break
    result = 0
    for y in yellow_list:
        if y[1]*2 + (y[0]+2)*2 == brown:
            answer.append(y[1]+2)
            answer.append(y[0]+2)
            break
        
    return answer
