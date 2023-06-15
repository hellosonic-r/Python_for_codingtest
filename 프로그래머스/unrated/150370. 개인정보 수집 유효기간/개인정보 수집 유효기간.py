def solution(today, terms, privacies):
    answer = []
    today = today.split(".") #문자열 형태임(오늘날짜)
    today_day = int(today[0])*28*12 + int(today[1])*28 + int(today[2]) #날짜를 일수로 변환
        
    #약관 종류 : 유효기간 -> 딕셔너리 저장
    d = {}
    for term in terms:
        term = term.split()
        d[term[0]] = int(term[1])
        
    for i in range(len(privacies)):
        temp = privacies[i].split() #["2021.05.02", "A"]
        date = temp[0].split(".") #["2021", "05", "02"]
        case = temp[1] #약관 유형
        date_day = int(date[0])*28*12 + int(date[1])*28 + int(date[2]) + d[case] * 28
        if date_day <= today_day:
            answer.append(i+1)
            
    
        
    
    return answer