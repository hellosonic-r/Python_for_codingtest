#이진수

#12 이진수로 표현 1100
#16 이진수로 표현 10000
#13 이진수로 표현 1101 3자리 1 / 2자리 1 / 1자리 0 / 0자리 1

t = int(input())
for i in range(t):
    n = int(input())

    bn_list = []

    while n != 1:
        if n % 2 == 1:
            bn_list.append(1)
            n //= 2
        else:
            bn_list.append(0)
            n //= 2
    bn_list.append(1)

    for j in range(len(bn_list)+1):
        if j == len(bn_list): # j 가 4이면 점프
            print()
        else:
            if bn_list[j] == 1:
                print(j,end = " ")
            else:
                continue