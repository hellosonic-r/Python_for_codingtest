###실패코드(왜틀렸는지 모르겠음)
t = 10
for test_case in range(1, t+1):
    dump = int(input())
    box_list = list(map(int, input().split()))
    while dump > 0:
        max_idx = box_list.index(max(box_list))
        min_idx = box_list.index(min(box_list))
        if box_list[max_idx] - box_list[min_idx] == 0:
            break
        else:
            box_list[max_idx] -= 1
            box_list[min_idx] += 1
            dump -= 1
    print("#{} {}".format(test_case, box_list[max_idx] - box_list[min_idx]))

###정답코드
t = 10
for test_case in range(1, t+1):
    dump = int(input())
    box_list = list(map(int, input().split()))
    while dump > 0:
        box_list.sort()
        if box_list[-1] - box_list[0] <= 1:
            break
        else:
            box_list[-1] -= 1
            box_list[0] += 1
            dump -= 1
    print("#{} {}".format(test_case, max(box_list)-min(box_list)))
        