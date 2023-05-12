n = int(input())
dice = []
for _ in range(n):
    dice_check = list(map(int, input().split()))
    x = dice_check.pop(5)
    dice_check.insert(3,x)
    dice.append(dice_check)

max_side = 0

for i in range(6):
    side = 0
    up = dice[0][i]
    down = dice[0][(i+3)%6]
    temp_list = []
    for j in range(6):
        if j == i or j == (i+3)%6:
            continue
        else:
            temp_list.append(dice[0][j])
    side += max(temp_list)
    next_down = dice[0][i] 
    d = 1
    while True:
        if d == n:
            break
        for k in range(6):
            s_down = next_down
            if dice[d][k] == s_down:
                s_up = dice[d][(k+3)%6]
                break
        tmp_list = []
        for z in range(6):
            if dice[d][z] == s_down or dice[d][z] == s_up:
                continue
            else:
                tmp_list.append(dice[d][z])
        side += max(tmp_list)
        next_down = s_up
        d+=1
    if max_side < side:
        max_side = side

print(max_side)
            

