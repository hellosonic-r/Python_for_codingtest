n, k = map(int, input().split()) #n: 전체 날짜 / k: 연속적인 날짜수
num_list = list(map(int ,input().split()))

result_list = [sum(num_list[0:k])]
for i in range(n-k):
    result_list.append(result_list[i]-num_list[i]+num_list[i+k])


print(max(result_list))