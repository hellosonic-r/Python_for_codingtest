# string = list(input())

# #입력받은 문자열의 길이를 저장
# len_string = len(string)

# #문자열의 길이의 약수를 구하는 코드 
# for i in range(1,len_string+1): # 6
#     #문자열의 길이의 약수인 i 중에서
#     if len_string % i == 0:
#         # 나누는 수(i)가 나눈 후의 몫(len_string // i)보다 작아야됨
#         # ex) 16 : 1, 16//1 = 16 / 2, 16//2 = 8
#         if i <= len_string //i:
#             #r = i(작은수), c = len_string//i(큰 수)
#             #조건을 충족한다면 r,c값은 갱신됨   
#             r = i
#             c = len_string // i
# #문자열을 담을 리스트 초기화
# ans = [[0]*r for _ in range(c)]
# cnt = 0
# for i in range(c):
#     for j in range(r):
#         ans[i][j] = string[cnt]
#         #입력한 문자열의 인덱스를 하나씩 증가시킨다
#         cnt += 1
        

# for i in range(r):
#     for j in range(c):
#         print(ans[j][i],end ="")
# print() 

string = list(input())

#입력받은 문자열의 길이를 저장
len_string = len(string)

#문자열의 길이의 약수를 구하는 코드 
for i in range(1,len_string+1): # 6
    #문자열의 길이의 약수인 i 중에서
    if len_string % i == 0:
        # 나누는 수(i)가 나눈 후의 몫(len_string // i)보다 작아야됨
        # ex) 16 : 1, 16//1 = 16 / 2, 16//2 = 8
        if i <= len_string //i:
            #r = i(작은수), c = len_string//i(큰 수)
            #조건을 충족한다면 r,c값은 갱신됨   
            r = i
            c = len_string // i
#문자열을 담을 리스트 초기화
ans = [[]*r for _ in range(c)]
cnt = 0
for i in range(c):
    for j in range(r):
        ans[i].append(string[cnt])
        #입력한 문자열의 인덱스를 하나씩 증가시킨다
        cnt += 1
        

for i in range(r):
    for j in range(c):
        print(ans[j][i],end ="")
print() 
