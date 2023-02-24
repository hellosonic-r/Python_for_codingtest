###숫자의 개수
a = int(input())
b = int(input())
c = int(input())
num = a * b * c

num_list = list(map(int, str(num))) #숫자의 각 자리를 리스트에 저장하기


fin_list = [0] * 10

for i in range(len(num_list)):
    x = num_list[i]
    fin_list[x] += 1

for i in range(10):
    print(fin_list[i]) 




#숫자의 각 자리를 리스트에 저장하기