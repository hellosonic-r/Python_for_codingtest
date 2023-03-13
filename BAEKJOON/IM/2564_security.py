# result = 0
# def find_distance(a,b, r, s):
#     global n, m, result 
#     if a == 1:
#         if r == 2:
#             result += min(b+m+s, (n-b)+m+(n-s))
#         elif r == 3:
#             result += b+s
#         elif r == 4:
#             result += n-b+s
#         elif r == 1:
#             result += abs(b-s)
#     elif a == 2:
#         if r == 1:
#             result += min(b+m+s, (n-b)+m+(n-s))
#         elif r == 3:
#             result += b+m-s
#         elif r == 4:
#             result += n-b+m-s
#         elif r == 2:
#             result += abs(b-s)
#     elif a == 3:
#         if r == 1:
#             result += b+s
#         elif r == 2:
#             result += m-b+s
#         elif r == 4:
#             result += min(b+n+s, (m-b)+n+(m-s))
#         elif r == 3:
#             result += abs(b-s)
#     elif a == 4:
#         if r == 1:
#             result += b+n-s
#         elif r == 2:
#             result += m-b+n-s
#         elif r == 3:
#             result += min(b+n+s, (m-b)+n+(m-s))
#         elif r == 4:
#             result += abs(b-s)

# n, m = map(int, input().split())
# how_many_store = int(input())

# direction_list = []
# distance_list = []
# for i in range(how_many_store):
#     direction, distance = map(int, input().split())
#     direction_list.append(direction)
#     distance_list.append(distance)
# dk_direction, dk_distance = map(int, input().split())


# for i in range(how_many_store):
#     find_distance(dk_direction,dk_distance,direction_list[i],distance_list[i])

# print(result)

#북쪽 왼쪽 모서리를 0으로 잡고 일자로 펼쳤을 때 얼마나 떨어졌는지 위치를 계산해주는 함수
def get_distance(x, y):
    if x == 1: #북
        return y
    if x == 2: #남
        return w + h + w - y
    if x == 3: #서
        return w + h + w + h - y
    if x == 4: #동
        return w + y
    
w, h = map(int, input().split())
n = int(input())

course = []
for _ in range(n+1): # (0,0)에서 상점까지의 거리
    x, y = map(int, input().split())
    course.append(get_distance(x,y))

answer = 0
for i in range(n): #동근이 거리 : course[-1]
    in_course = abs(course[-1] - course[i])
    out_course = 2 * (w + h) - in_course
    answer += min(in_course, out_course)

print(answer)