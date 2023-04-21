t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    distance = 0
    speed = 0
    for _ in range(n):
        command_list = list(input())
        if ' ' in command_list:
            if int(command_list[0]) == 1:  # 1 가속 2 감속 / 뒤에 오는거 가속도 1 혹은 2
                speed += int(command_list[2])
            elif int(command_list[0]) == 2:
                speed -= int(command_list[2])
                if speed < 0:
                    speed = 0
            distance += speed
        else: #0일때
            distance += speed
    print("#{} {}".format(test_case, distance))
        