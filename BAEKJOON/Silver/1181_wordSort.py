n = int(input())
word_list = []
for _ in range(n):
    string = input()
    word_list.append(string)

word_list = list(set(word_list)) #set -> list 로 중복 제거
word_list.sort() #문자열을 요소로 갖는 리스트를 정렬하면, 길이가 아닌 앞글자의 사전 순으로 정렬된다.
word_list = sorted(word_list, key = lambda x: len(x)) #길이 순으로 정렬

for i in word_list:
    print(i)