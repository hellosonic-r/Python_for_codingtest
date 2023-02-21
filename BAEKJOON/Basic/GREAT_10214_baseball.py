import sys
T = int(input())

for i in range(T):
    y_score_list = []
    k_score_list = []
    for j in range(9):
        y_score, k_score = map(int, sys.stdin.readline().split())
        y_score_list.append(y_score)
        k_score_list.append(k_score)
    print("Yonsei" if sum(y_score_list) > sum(k_score_list) \
          else ("Korea" if sum(k_score_list) > sum(y_score_list) else "Draw"))
        