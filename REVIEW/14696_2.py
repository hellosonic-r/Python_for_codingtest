n = int(input())
for _ in range(n):
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    a_list.pop(0)
    b_list.pop(0)
    a_list.sort(reverse=True)
    b_list.sort(reverse=True)
    if a_list > b_list:
        print("A")
    elif a_list < b_list:
        print("B")
    else:
        print("D")