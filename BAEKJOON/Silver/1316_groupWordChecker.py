n = int(input())

#그룹 단어의 개수 : 총 단어의 개수로 초기화 
total_cnt = n
for _ in range(n):
    string = list(input())
    #26개의 알파벳만큼 리스트를 생성 (a=idx0 / b=idx1 ...)
    #알파벳 리스트의 인덱스는 <알파벳을 아스키코드로 변환한 값 - 97> 이다.
    alpha = [[] for _ in range(26)]
    #현재 누적된 글자 개수는 1
    cnt = 1
    #단어 글자를 하나하나 뜯어보며 분석
    for i in range(len(string)):
        #첫 번째 글자는 누적된 글자 개수가 1이다.
        if i == 0:
            #알파벳 리스트에 누적된 글자 개수 저장
            alpha[ord(string[i])-97].append(cnt)
        else:
            #만약 이전 글자하고 같다면
            if string[i] == string[i-1]:
                #누적된 글자 개수를 1 증가시키고
                cnt+=1
                #알파벳 리스트에 누적된 글자 개수 추가
                alpha[ord(string[i])-97].append(cnt)
            #만약 이전 글자하고 다르다면
            else:
                #누적된 글자 개수를 1로 갱신하고
                cnt = 1
                #알파벳 리스트에 누적된 글자 개수 1 추가
                alpha[ord(string[i])-97].append(cnt)
    
    
    for i in range(len(alpha)):
        #알파벳이 없는 곳은 통과
        if len(alpha[i]) == 0:
            continue
        else:
            #누적된 글자 개수의 최댓값이 리스트길이(단어에서 총 등장한 글자 개수)와 다르면
            if max(alpha[i]) != len(alpha[i]):
                #그룹 단어의 개수에서 1을 빼고 반복문 탈출
                total_cnt -= 1
                break

print(total_cnt)


n = int(input())

group_word = 0
for i in range(n):
    word = input()
    error = 0
    for j in range(len(word)-1):
        #만약 현재 글자가 다음 글자와 같지 않다면
        if word[j] != word[j+1]:
            #다음 글자부터 나머지 글자까지의 문자열을 만들고
            new_word = word[j+1:]
            #그 문자열에 현재 글자가 포함되어 있는지 확인한다.
            if new_word.count(word[j]) > 0:
                error += 1
    if error == 0:
        group_word +=1
print(group_word)
