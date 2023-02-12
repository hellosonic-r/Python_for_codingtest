score_list = []
for i in range(5):
    score = int(input())
    score_list.append(score) #선언한 리스트 <score_list> 에 요소 <score> 넣기
    for j in range(len(score_list)):
        if score_list[j] < 40:
            score_list[j] = 40
print(sum(score_list) // int(len(score_list))) #sum함수의 변수에 리스트 넣기
