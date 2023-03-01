###안테나
##내풀이
# n = int(input())
# houses = list(map(int, input().split()))
# houses.sort()
# fin = []
# for i in range(1, houses[n-1]): #안테나를 설치할 위치 체크
#     distance = 0
#     for house in houses: #house에서 안테나까지의 거리를 하나씩 비교
#         distance += abs(house - i) 
#     fin.append((distance, i))

# fin.sort()
# print(fin[0][1])

##교재풀이(중간값에 안테나 위치한다고 가정)
n = int(input())
data = list(map(int, input().split()))
data.sort()
#중간값 출력
print(data[(n-1)//2])