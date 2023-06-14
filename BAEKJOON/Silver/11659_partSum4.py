import sys

n, m = map(int, input().split())
num_list = list(map(int, sys.stdin.readline().split())) # [5 4 3 2 1]

#인덱스 혼동되지 않기 위해 n+1 길이의 합을 저장할 리스트 생성
prefix_sum = [0 for _ in range(n+1)] #[0,0,0,0,0,0]

#리스트에 누적된 합을 저장하는 소스 코드
for i in range(n): 
    prefix_sum[i+1] = prefix_sum[i] + num_list[i]

for _ in range(m):
    start, end = map(int, sys.stdin.readline().split())
    #누적된 합이 저장된 리스트의 (end 인덱스에 해당하는 값) - (start-1 인덱스에 해당하는 값)
    #                   = 구하려는 구간의 누적 합
    print(prefix_sum[end] - prefix_sum[start-1]) 
