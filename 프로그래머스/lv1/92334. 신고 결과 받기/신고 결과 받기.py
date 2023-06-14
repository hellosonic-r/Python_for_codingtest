def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    check = [0 for _ in range(len(id_list))] #신고 받은 횟수
    who = [[] for _ in range(len(id_list))] #신고자 리스트
    
    report = list(set(report))
    for i in report: #리포트 신고내역 하나씩 분석
        r_arr = list(map(str, str(i)))
        idx_space = r_arr.index(" ")
        to = "".join(map(str, r_arr[:idx_space]))
        fro = "".join(map(str, r_arr[idx_space+1:]))
        idx = id_list.index(fro)
        check[idx] += 1
        who[idx].append(to)

    for j in range(len(id_list)):
        if check[j] >= k:
            for z in who[j]:
                answer[id_list.index(z)] += 1
        
    
    return answer