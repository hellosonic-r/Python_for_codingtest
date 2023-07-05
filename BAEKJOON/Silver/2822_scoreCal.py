score_list = []
for _ in range(8):
    score_list.append(int(input()))

ans = 0
num = []

while len(num)<5:
    temp = 0
    idx = 0
    for i in range(8):
        if i+1 not in num:
            if temp < score_list[i]:
                temp = score_list[i]
                idx = i+1
    num.append(idx)
    ans += temp

num.sort()
print(ans)
print(" ".join(map(str, num)))
