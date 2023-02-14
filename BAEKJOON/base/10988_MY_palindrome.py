word = input() #문자 하나하나가 리스트에 저장 #soon 을 넣어보자
word_list = [] #빈 리스트
for i in range(len(word)): #range(4) #len(word)는 4 #0,1,2,3
    if word[i] == word[len(word)-i-1]: #i가 0일때 word[0] == word[3] #i가 3일때 word[3] == word[0]
        word_list.append(1)

    else:
        word_list.append(0)

print(0 if word_list.count(0) >= 1 else 1)