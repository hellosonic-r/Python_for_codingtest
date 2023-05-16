for test_case in range(1, 11):
    count = int(input())
    num_list = list(map(int, input().split()))
    num_list.sort(reverse = True) #내림차순 정렬

    n = 0
    while n < count:
        num_list.sort(reverse=True)  #덤프를 실시할 때마다, 최고점을 앞으로, 최저점을 뒤로 보내는 정렬 실시
        n += 1 #덤프 횟수 증가
        num_list[0] -= 1 #최고점을 1 깎는다
        num_list[-1] += 1 #최저점에 1 쌓는다
        #만약 덤프할 게 없다면 반복문탈출
        if max(num_list) - min(num_list) == 1 or max(num_list) - min(num_list) == 0:
            break

    print("#{} {}".format(test_case, (max(num_list) - min(num_list))))
