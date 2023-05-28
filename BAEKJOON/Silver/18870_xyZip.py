n = int(input())
num_list = list(map(int, input().split()))
sorted_num_list = sorted(num_list) #입력받은 숫자들을 정렬한다.

d = {} #빈 딕셔너리 생성

k = 0 #압축 숫자
for i in range(len(sorted_num_list)): #정렬된 숫자들을 돌면서
    if sorted_num_list[i] not in d: #딕셔너리에 추가가 안된 숫자라면
        d[sorted_num_list[i]] = k #딕셔너리에 압축 숫자를 넣는다
        k += 1 #딕셔너리에 신규 키값 들어올때마다 1씩 증가

for i in range(len(num_list)): #원본 숫자 리스트들을 돌면서
    print(d[num_list[i]], end = " ") #딕셔너리에 저장된 값 출력한다.

print()

