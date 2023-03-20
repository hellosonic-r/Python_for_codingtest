king, stone, n = input().split()
chess = [[0] * 8 for _ in range(8)]
king_list = list(king) #["A","1"]
stone_list = list(stone)

king = [ord(king_list[0])-65, int(king_list[1])-1]
stone = [ord(stone_list[0])-65, int(stone_list[1])-1]


# T R B L / LT RT RB LB
# dx = [0,1,0,-1,-1,1,1,-1] 
# dy = [1,0,-1,0,1,1,-1,-1]
dir_x = {"T":0, "R":1, "B":0, "L":-1, "LT":-1, "RT":1, "RB":1, "LB":-1}
dir_y = {"T":1, "R":0, "B":-1, "L":0, "LT":1, "RT":1, "RB":-1, "LB":-1}

king_nx, king_ny, stone_nx, stone_ny = 0,0,0,0
for _ in range(int(n)):
    direction = input()
    king_nx = king[0] + dir_x[direction]
    king_ny = king[1] + dir_y[direction]
    stone_nx = stone[0] + dir_x[direction]
    stone_ny = stone[1] + dir_y[direction]
    #이동 후의 킹이 범위를 벗어나면 다음 이동 수행
    if king_nx < 0 or king_nx > 7 or king_ny < 0 or king_ny > 7:
        continue
    #벗어나지 않는다면
    else:
        #킹이 가는 방향에 돌이 있다면
        if king_nx == stone[0] and king_ny == stone[1]:  
            #이동 후의 돌이 범위를 벗어나면 다음 이동 수행
            if stone_nx < 0 or stone_nx > 7 or stone_ny < 0 or stone_ny > 7:
                continue
            #벗어나지 않는다면 킹, 돌 이동
            else:
                king[0],king[1] = king_nx, king_ny
                stone[0],stone[1] = stone_nx, stone_ny
        #킹이 가는 방향에 돌이 없다면
        else:
            #킹만 이동
            king[0],king[1] = king_nx, king_ny

print(chr(king[0]+65),king[1]+1,sep="")
print(chr(stone[0]+65),stone[1]+1,sep="")



