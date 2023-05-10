t = int(input())
for test_case in range(1, t+1):
    n, q = map(int, input().split()) #1~n까지 상자, Q번 반복
    num_list = [0] * (n+1)
    for i in range(1,q+1):
        l, r = map(int, input().split())
        for j in range(l, r+1):
            num_list[j] = i
    num_list.pop(0)
    print("#{} {}".format(test_case, " ".join(map(str, num_list))))
        