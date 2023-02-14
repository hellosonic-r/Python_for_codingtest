###36ms으로 1등
import sys
n = int(input())
Q1,Q2,Q3,Q4,AXIS = [],[],[],[],[] # 40ms -> 36ms

for i in range(n):
    x,y = map(int, sys.stdin.readline().split())
    if x>0 and y>0:
        Q1.append(1)
    elif x<0 and y>0:
        Q2.append(1)
    elif x<0 and y<0:
        Q3.append(1)
    elif x>0 and y<0:
        Q4.append(1)
    else:
        AXIS.append(1)
print("Q1: {}\nQ2: {}\nQ3: {}\nQ4: {}\nAXIS: {}"\
      .format(Q1.count(1),Q2.count(1),Q3.count(1),Q4.count(1),AXIS.count(1)))