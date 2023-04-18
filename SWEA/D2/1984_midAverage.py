t = int(input())

for test_case in range(1, t+1):
    num_list = list(map(int, input().split()))
    num_list.remove(max(num_list))
    num_list.remove(min(num_list))
    ans = sum(num_list) / len(num_list)
    print("#{} {}".format(test_case, int(round(ans,0))))