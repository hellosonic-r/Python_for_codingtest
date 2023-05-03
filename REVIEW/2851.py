score_list = []
for _ in range(10):
    score_list.append(int(input()))

ans = 0
score_sum = 0
for i in range(len(score_list)):
    score_sum += score_list[i]
    if i == 0 and score_sum == 100:
        ans = 100
        break
    if i != 0 and score_sum >= 100:
        if abs(score_sum - 100) < abs(score_sum - score_list[i] - 100):
            ans = score_sum
        elif abs(score_sum - 100) > abs(score_sum - score_list[i] - 100):
            ans = score_sum - score_list[i]
        else: 
            ans = score_sum
        break
    
if ans == 0:
    print(sum(score_list))
else:
    print(ans)
