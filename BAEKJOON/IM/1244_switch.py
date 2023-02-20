n = int(input())
switch_status = list(map(int, input().split()))
students = int(input())
sex_num = []
for _ in range(students):
    sex, num = map(int, input().split())
    sex_num.append((sex, num))

def turn_switch(i):
    global switch_status
    switch_status[i] += 1
    if switch_status[i] == 2:
        switch_status[i] = 0

for i in range(1, (len(switch_status)+1)):
    for a in range(students):
        if sex_num[a][0] == 1:
            if i % num == 0:
                turn_switch(i-1)
        elif sex_num[a][0] == 2:
            must_change_index = []
            j = 1
            if i == num:
                must_change_index.append(i-1)
                while True:
                    if i-1-j < 0 or i-1+j > n-1:
                        break
                    elif switch_status[i-1-j] == switch_status[i-1+j]:
                        must_change_index.append(i-1-j)
                        must_change_index.append(i-1+j)
                    j += 1
            for k in must_change_index:
                turn_switch(k)
print(must_change_index)
for z in range(n):
    print(int(switch_status[z]),end = " ")
    if z % 20 == 19:
        print()        
print()
