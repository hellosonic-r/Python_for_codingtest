# import sys

# N = int(input())
# v_list=[]

# for i in range(N):
#     v = list(map(int, sys.stdin.readline().split())) ## map은 출력기능이 없음
#     v_list.append(v)

# print("Junhee is cute!" if v_list.count([1]) > v_list.count([0]) else "Junhee is not cute!")


import sys

N = int(input())
v_list=[]

for i in range(N):
    #v = list(map(int, input().split())) ## map 은 출력 기능이 없고 메모리 상에서만 연산한다
                                         ## list 를 씌워줌으로써 출력 가능하게 한다.
    v = int(input())                     ## 혹은 map 쓰지 않아야 한다.
    v_list.append(v)
print(v_list)

print("Junhee is cute!" if v_list.count(1) > v_list.count(0) else "Junhee is not cute!")