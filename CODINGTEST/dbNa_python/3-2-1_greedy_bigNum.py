###단순하게 풀기
n, m, k = map(int, input().split()) #5,8,3 / 8의 길이 리스트. 같은 수 최대 3번 반복 /

data = sorted(list(map(int, input().split()))) #2,4,5,4,6
data.sort(reverse=True) #6,5,4,4,2

fin_list = [] #정답 수열을 보기 위해 리스트 선언
while True:
    for i in range(k): #가장 큰 수를 3번 더하기
        if m == 0: #8의 길이가 0이 되면 반복문 탈출
            break
        fin_list.append(data[0]) #가장큰수를 리스트에 추가
        m -= 1 #숫자 하나를 저장할때마다 8의 길이 - 1
    if m == 0:
        break
    fin_list.append(data[1])
    m -= 1

print(fin_list)
        