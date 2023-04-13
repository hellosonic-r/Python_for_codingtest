import sys

n = int(sys.stdin.readline())
switch = [0] + list(map(int, sys.stdin.readline().split()))

student = int(sys.stdin.readline())

for _ in range(student):
    sex, num = map(int, sys.stdin.readline().split())
    if sex == 1:
        check = (len(switch)-1) // num #9-1 = 8 -> 2
        for i in range(1, check+1):
            switch[num*i]=abs(switch[num * i]-1)
    elif sex == 2: 
        switch[num] = abs(switch[num]-1)
        check_2 = min(num-1, len(switch)-1-num)
        for i in range(1, check_2 + 1):
            if switch[num-i] == switch[num+1]:
                switch[num-i]=abs(switch[num-i]-1)
                switch[num+i]=abs(switch[num+i]-1)
            else:
                break
            
switch.pop(0)

for i in range(len(switch)):
    if i!=0 and i % 20 == 0:
        print()
    print(switch[i], end = " ")
print()

        
