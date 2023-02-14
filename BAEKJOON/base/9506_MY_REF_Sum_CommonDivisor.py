###잘 푼 것 같은데 출력 형식이 잘못되었다고 한다.
while True:
    n = int(input())
    answer = 0
    n_list = []
    if n == -1:
        break
    else:
        for i in range(n):
            if i == 0:
                continue
            elif n % i == 0:
                n_list.append(i)
            else:
                continue

    if n != sum(n_list):
        print(n,"is NOT perfect.")
    else:
        print(n," = ",end = " ")
        for j in range(len(n_list)):
            if j == (len(n_list))-1: #print 마지막에는 + 빼주기
                print(n_list[j])
            else:
                print(n_list[j],end=" + ")
