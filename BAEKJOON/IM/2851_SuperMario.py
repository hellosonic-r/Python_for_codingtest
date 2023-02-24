###슈퍼마리오
##내풀이
# score = []
# score_sum_list = []
# score_sum = 0
# for i in range(10):
#     score.append(int(input()))
#     score_sum += score[i]
#     score_sum_list.append(score_sum)

# if score_sum_list[9] <= 100:
#     print(score_sum_list[9])
# else:
#     for i in range(10):
#         if score_sum_list[i] == 100:
#             print(score_sum_list[i])
#             break
#         else:
#             if 100 - score_sum_list[i] < 0:
#                 if 100 - score_sum_list[i-1] < score_sum_list[i] - 100:
#                     print(score_sum_list[i-1])
#                 elif 100 - score_sum_list[i-1] > score_sum_list[i] - 100:
#                     print(score_sum_list[i])
#                 elif 100 - score_sum_list[i-1] == score_sum_list[i] - 100:
#                     print(max(score_sum_list[i-1],score_sum_list[i]))
#                 break

##다른사람 풀이
import sys

result = 0
score = 0
for _ in range(10):
    n = sys.stdin.readline()
    score += n
    if 100 - result >= abs(100 - score):
        result = score

print(result)