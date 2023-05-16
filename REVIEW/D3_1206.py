for test_case in range(1, 11):
    n = int(input()) #건물의 개수
    num_list = list(map(int, input().split()))
    ans = 0
    for i in range(2, len(num_list)-2):
        if num_list[i] > max(num_list[i-2], num_list[i-1], num_list[i+1], num_list[i+2]):
            ans += (num_list[i] - max(num_list[i-2], num_list[i-1], num_list[i+1], num_list[i+2]))
    print(ans)