T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    num_list = list(map(int, input().split()))
    ans = 0
    ans = round(sum(num_list) / 10)
    print("#{0} {1}".format(test_case, ans))
