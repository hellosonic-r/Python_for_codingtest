word = input().upper()
word_list = list(set(word))

cnt = []
for i in word_list:
    cnt.append(word.count(i))

if cnt.count(max(cnt)) >= 2:
    print("?")

else:
    print(word_list[cnt.index(max(cnt))])

# 리스트의 최대값의 인덱스 구할 수 있다.
# upper() 함수를 사용할 수 있다.