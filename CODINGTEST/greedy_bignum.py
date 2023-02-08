#큰 수의 법칙
'''
N : 배열의 크기
M : 숫자가 더해지는 횟수
K : 한 번에 더할 수 있는 횟수
'''

n, m, k = map(int, input().split()) #n,m,k 를 공백으로 구분하여 입력받기
data = list(map(int, input().split())) #n개의 자연수를 공백으로 구분하여 입력받기

data.sort() #입력받은 수들을 오름차순으로 정렬
first_big = data[n-1] #입력한 자연수 중 가장 큰 수
second_big = data[n-2] #두번째로 큰 수

result = 0 

while True:
    for i in range(k): #가장 큰 수를 k번 더하기
        if m == 0: #m 이 0 이면 반복문 탈출
            break
        result = result + first_big #가장 큰 수를 k번 더한 결과를 result에 저장
        m = m - 1 #더할때마다 m을 1씩 빼기
    # 3번 다 더했다면 for문 나가기

    if m == 0: #m이 0인지 확인
        break #while 문에 대한 break
    result = result + second_big #m이 0이 아니라면 두번째 큰 수를 result에 저장
    m = m - 1 #m을 1빼기
    #while true 문으로 인해 반복문 다시 실행

print(result)


