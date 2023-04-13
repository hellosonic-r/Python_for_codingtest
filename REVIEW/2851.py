ans = 0
score_list = []
for _ in range(10):
    score_list.append(int(input()))

i = 0
ans = 0
idx = 0
while True:
    if i == 10:
        break
    ans += score_list[i]
    if ans > 100:
         break
    i += 1

if i == 10:
    print(ans)
else:
    if ans - 100 < abs(ans-score_list[i]-100):
        print(ans)
    elif ans - 100 > abs(ans-score_list[i]-100):
        print(ans)
    else:
        print(ans)

