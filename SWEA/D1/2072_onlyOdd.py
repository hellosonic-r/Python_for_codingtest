T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

for test_case in range(1, T + 1):
    ans = 0 
    num_list = list(map(int, input().split()))
    for num in num_list:
        if num % 2 == 1:
            ans += num
        else: 
            continue
    print("#{0} {1}".format(test_case, ans))