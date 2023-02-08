#큰 수의 법칙 m이 100억이상일때
'''
N : 배열의 크기
M : 숫자가 더해지는 횟수
K : 한 번에 더할 수 있는 횟수
{6,6,6,5}
'''

n,m,k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first_big = data[n-1]
second_big = data[n-2]


count = int(m/(k+1)) * k #가장 큰 수가 더해지는 횟수 계산
count = count + m % (k+1) #횟수가 나누어 떨어지지 않을 수 있으므로

result = 0 
result = result + (count) * first_big #가장 큰 수 더하기
result = result + (m - count) * second_big #두 번째로 큰 수 더하기

print(result)
