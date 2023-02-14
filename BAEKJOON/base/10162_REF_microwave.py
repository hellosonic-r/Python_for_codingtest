###리스트 이용
t = int(input())

oper_time = [300,60,10]
fin = []

if t % 10 != 0:
    print(-1)
else:
    for i in oper_time:
        count = t // i
        fin.append(count)
        t = t % i
    print(fin[0],fin[1],fin[2],sep = " ")