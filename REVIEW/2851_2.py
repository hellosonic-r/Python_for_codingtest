score_list = []
for _ in range(10):
    score_list.append(int(input()))

ans = 0
score_sum = 0
for i in range(10):
    score_sum += score_list[i]
    if score_sum == 100:
        ans = score_sum 
        break
    if score_sum > 100:
        if score_sum-100 <= 100-(score_sum-score_list[i]):
            ans = score_sum
        else:
            ans = score_sum-score_list[i]
        break
    ans += score_list[i]

print(ans)
