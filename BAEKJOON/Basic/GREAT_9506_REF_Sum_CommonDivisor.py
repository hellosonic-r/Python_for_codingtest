###다시해보니 맞았음
while True:
    n = int(input())
    if n == -1:
        break
    else:
        n_list = []
        for i in range(n):
            if i == 0:
                continue
            elif n % i == 0:
                n_list.append(i)
            else:
                continue
        if n != sum(n_list):
            print("{} is NOT perfect.".format(n))
        else:
            print(n,"= ",end="")
            for j in range(len(n_list)):
                if j == len(n_list) - 1: ###꿀팁 
                    print(n_list[j])
                else:
                    print(n_list[j],end=" + ")