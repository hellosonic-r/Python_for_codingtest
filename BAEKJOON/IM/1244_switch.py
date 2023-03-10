def switching(a, b):
    #남학생
    if a == 1:
        for i in range(1, len(switch_status)):
            if i % b == 0:
                switch_status[i] = abs(switch_status[i] - 1)
            else:
                continue
    #여학생
    elif a == 2:
        switch_status[b] = abs(switch_status[b] - 1)
        j = 1
        while True:
            if b-j == 0 or b+j == len(switch_status):
                break
            else:
                if switch_status[b-j] == switch_status[b+j]:
                    switch_status[b-j] = abs(switch_status[b-j] - 1)
                    switch_status[b+j] = abs(switch_status[b+j] - 1)
                    j += 1
                else:
                    break

n = int(input())
switch_zero = [0]
switch = list(map(int, input().split()))
switch_status = switch_zero + switch

how_many_students = int(input())

for _ in range(how_many_students):
    sex, num = map(int, input().split())
    switching(sex, num)
switch_status.pop(0)

for i in range(len(switch_status)):
    if i != 0 and i % 20 == 0:
        print()
    print(switch_status[i],end =" ")
    if i == len(switch_status) - 1:
        print()
    