###시각 #3이 포함
##솔 실패 

h = int(input()) ## h시 59분 59초

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            #시,분,초를 문자열 자료형으로 바꾸어 합치고 3이 해당 문자열에 포함되는지 확인한다.
            if '3' in (str(i) + str(j) + str(k)):
                count += 1
print(count)

    

