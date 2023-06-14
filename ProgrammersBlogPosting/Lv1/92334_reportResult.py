##나의 코드 
def solution(id_list, report, k):
    #각 유저가 k번 이상 신고당한다면, 그 유저를 신고한 사람에게 메일이 전달되고, 
    #answer 리스트는 각 유저별 메일을 받은 횟수를 저장
    answer = [0 for _ in range(len(id_list))] 
    check = [0 for _ in range(len(id_list))] #각 유저가 신고받은 횟수
    who = [[] for _ in range(len(id_list))] #각 유저를 신고한 신고자 리스트

    #set으로 중복을 제거해준다(한 유저가 다른 유저를 여러 번 신고할 경우 카운트 되는 것을 방지)
    report = list(set(report))

    #리포트 신고내역 하나씩 분석
    for i in report: 
        r_arr = list(map(str, str(i)))
        idx_space = r_arr.index(" ") #공백을 기준으로 좌 우 문자열을 나누기 위함
        to = "".join(map(str, r_arr[:idx_space])) #공백을 기준으로 좌측 문자열
        fro = "".join(map(str, r_arr[idx_space+1:])) #공백을 기준으로 우측 문자열
        idx = id_list.index(fro) #신고받은 사람의 인덱스
        check[idx] += 1 #각 유저가 신고받은 횟수 카운트
        who[idx].append(to) #신고를 누가했는지 who 리스트에 저장

    for j in range(len(id_list)): #모든 유저를 살펴보면서
        if check[j] >= k: #check리스트(각 유저가 신고받은 횟수를 저장한 리스트) 원소가 k이상이라면
            for z in who[j]: #who 리스트에서 누가 신고했는지 본다.
                answer[id_list.index(z)] += 1 #신고한 유저는 메일을 받으므로 answer 원소값을 카운트+1 해준다.
        
    
    return answer

##다른 코드
def solution(id_list, report, k):
    answer = [0] * len(id_list) #메일 받은 횟수
    reports = {x : 0 for x in id_list} #신고 받은 횟수 
    #{"무지":0, "프로도":0, "어피치":0, "네오":0} 

    for r in set(report):
        reports[r.split()[1]] += 1 #r.split() : 공백을 기준으로 나누기

    for r in set(report):
        if reports[r.split()[1]] >= k: #신고받은 횟수가 k회 이상이라면
            answer[id_list.index(r.split()[0])] += 1 #신고한 사람에 해당하는 answer 원소값에 +1

    return answer 

