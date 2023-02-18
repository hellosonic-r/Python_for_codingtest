###수학적 공식 계산해서 풀기
n, m, k = map(int, input().split()) #5,6,3
num = sorted(list(map(int, input().split()))) #2,4,5,4,6
num.sort(reverse=True)

count1 = m // (k+1) * k #가장 큰 수가 더해지는 횟수 == 6
result_first = 0
result_second = 0
if m % (k+1) == 0:
    result_first = count1 * num[0]
    result_second = m // (k+1) * num[1]
    print(result_first+result_second)
else:
    result_first = count1 * num[0]
    result_second = m // (k+1) * num[1]
    result_first = result_first + (m-(k+1)) * num[0]
    print(result_first + result_second)
