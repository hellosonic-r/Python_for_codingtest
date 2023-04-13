t = int(input())

for test_case in range(1, 1+t):
    num_li = list(map(int, str(input())))
    max_li = num_li
    min_li = num_li
    sorted_num_li = sorted(num_li)
    for i in range(1, len(max_li) + 1):
        if max_li[i-1] == sorted_num_li[-i]:
            continue
        else:
            must_change_idx = i-1
            max_value = sorted_num_li[-i]
    max_li[must_change_idx], max_li[max_li.index(max_value)] = max_li[max_li.index(max_value)], max_li[must_change_idx]
    
    print(max_li)
    
    # zero_count = sorted_num_li.count(0)
    # min_idx = zero_count # 정렬된 곳에서
    # if 0 in sorted_num_li:
    #     if min_li[0] != sorted_num_li[min_idx]:
    #         min_li[0], min[min_li.index(sorted_num_li[min_idx])] = min[min_li.index(sorted_num_li[min_idx])], min_li[0]
    #     else:
    #         temp_sorted_num_li = sorted_num_li
    #         temp_sorted_num_li.pop(min_idx)
    #         for i in range(1, len(min_li)):
    #             if min_li[i] == temp_sorted_num_li[i-1]:
    #                 continue
    #             else:
    #                 min_li[i], min_li[min_li.index(temp_sorted_num_li[i-1])] = min_li[min_li.index(temp_sorted_num_li[i-1])], min_li[i]
    #                 break
    # else:
    #     for i in range(len(min_li)):
    #         if min_li[i] == sorted_num_li[i]:
    #             continue
    #         else:
    #             min_li[i], min_li[min_li.index(sorted_num_li[i])] = min_li[min_li.index(sorted_num_li[i])], min_li[i]
    # print(max_li, min_li)
    