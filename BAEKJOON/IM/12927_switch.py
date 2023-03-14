# l = ['N']
# light = list(input()) # yyyy

# light_list = l + light # n yyyy #2번 스위치는 2, 4 끔 j % i == 0:
# def onoff(x):
#     if light_list[x] == 'Y':
#         light_list[x] = 'N'
#     elif light_list[x] == 'N':
#         light_list[x] = 'Y'

# count = 0
# while True:
#     if 'Y' not in light_list:
#         print(count)
#         break
#     for i in range(1, len(light_list)): # 1
#         for j in range(i, len(light_list)): # 1 2 3 4
#             if j % i == 0:
#                 onoff(j)
#         count += 1
#         if 'Y' not in light_list:
#             break
#         else:
#             continue


switch = [0] + list(input())
cnt = 0

for i in range(1, len(switch)):
    if switch == [0] + ['N'] * (len(switch)-1):
        break
    if switch[i] == 'N':
        continue
    for j in range(i, len(switch)):
        if j % i == 0:
            if switch[j] == 'Y':
                switch[j] = 'N'
            else:
                switch[j] = 'Y'
    cnt += 1
print(cnt)