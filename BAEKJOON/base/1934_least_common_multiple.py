T = int(input())
a_num = 1
b_num = 1
for i in range(T):
    a, b = map(int, input().split())
    while a != 1:
        if a % a_num == 0:
            print(a_num)
            a
        else:
            a_num += 1