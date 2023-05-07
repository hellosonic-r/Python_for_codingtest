t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    first_list = list(input())
    goal_list = list(input())
    compare = []
    for i in range(n):
        if first_list[i] != goal_list[i]: #초기 상태와 목표 상태가 다를 때, 
            compare.append(first_list[i]) #다른 말을 리스트에 넣는다.

    print(max(compare.count("W"),compare.count("B"))) #W와 B중 많은 것의 개수를 출력한다.
