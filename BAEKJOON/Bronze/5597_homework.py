num_list = [0] * 31

for i in range(28):
    num_list[int(input())] = 1

for i in range(1,31):
    if num_list[i] == 0:
        print(i)
