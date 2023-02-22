###참외밭
##런타임에러
# import sys

# k = int(input())
# field_list = [list(map(int, sys.stdin.readline().split())) for _ in range(6)]

# wide = 0
# wide_idx = 0
# height = 0
# height_idx = 0

# for i in range(len(field_list)):
#     if field_list[i][0] == 1 or field_list[i][0] == 2: #세로
#         if height < field_list[i][1]:
#             height = field_list[i][1]
#             height_idx = i
#     elif field_list[i][0] == 3 or field_list[i][0] == 4: #가로
#         if wide < field_list[i][1]:
#             wide = field_list[i][1]
#             wide_idx = i

# small_wide = abs(field_list[wide_idx-1][1] - field_list[wide_idx+1][1])
# small_height = abs(field_list[height_idx-1][1] - field_list[height_idx+1][1])

# print(k * (wide * height - small_wide * small_height))


###################다른풀이
# import sys 
# k = int(input())

# height = []
# width = []
# total = []

# for i in range(6):
#     dir, length = map(int, sys.stdin.readline().split())
#     if dir == 1 or dir == 2: #동, 서
#         width.append(length)
#         total.append(length)
#     else:
#         height.append(length)
#         total.append(length)
# print(height, width)
# print(total)
# bigbox = max(height) * max(width)

# maxh_idx = total.index(max(height)) #total.index(50) = 0
# maxw_idx = total.index(max(width)) #total.index(160) = 1



# small1 = abs(total[maxh_idx - 1] - total[(maxh_idx-5 if maxh_idx == 5 else \
#                                         maxh_idx + 1)])
# # 100  
# small2 = abs(total[maxw_idx - 1] - total[(maxw_idx-5 if maxw_idx == 5 else \
#                                          maxw_idx + 1)])

# # print(k * (bigbox - (small1 * small2)))


k = int(input())

height = []
width = []
total = []

for _ in range(6):
    direction, meter = map(int, input().split())
    if direction == 3 or direction == 4:
        height.append(meter)
        total.append(meter)
    else:
        width.append(meter)
        total.append(meter)

big_box = max(height) * max(width)

small_width = total[(total.index(max(height)) + 3) % 6]
small_height = total[(total.index(max(width)) + 3) % 6]

print(k * (big_box - (small_height * small_width)))