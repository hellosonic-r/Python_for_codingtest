n = int(input())
for _ in range(n):
    string_list = list(map(str,input().split()))
    for i in string_list:
        print(i[::-1], end = " ")
    print()