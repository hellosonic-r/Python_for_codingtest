t = int(input())

for test_case in range(1, t+1):
    num_list = list(map(int, input().split()))
    num_list.sort()
    a = num_list[0]
    b = num_list[-1]
    if a == b:
        ans = a
    else:
        if num_list.count(a) > num_list.count(b):
            ans = b
        else:
            ans = a

    print("#{} {}".format(test_case, ans))