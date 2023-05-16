# ##백트래킹, 시간초과..
# def dfs(count,temp_list):
#     if count == len(string):
#         if temp_list == temp_list[::-1]:
#             result.append("".join(map(str, temp_list)))
#         return
#     if count == 50:
#         return
#     for i in range(len(string)):
#         if v[i] == 0:
#             v[i] = 1
#             dfs(count+1, temp_list + [string[i]])
#             v[i] = 0

# string = list(input())
# v = [0] * len(string)

# result = []
# dfs(0, [])
# result.sort()

# if result:
#     print(result[0])
# else:
#     print("I'm Sorry Hansoo")



# #아스키 코드로 변환해보고 홀수가 2개 이상이면 팰린드롬을 만들 수 없다. ex) ABCCC
# #홀수가 1개 이하라면 팰린드롬이 가능하다 AABBC
# string = list(input())
# alpha_cnt = [0] * 26
# for alpha in string:
#     alpha_cnt[ord(string)-65] += 1

# odd = 0 #홀수
# odd_alpha = ""
# alpha = ""
# for i in range(26):
#     if alpha_cnt[i] % 2 == 1:
#         odd += 1
#         odd_alpha += chr(i+65)
#     alpha += chr(i+65) * (alpha_cnt[i] // 2)
    
# if odd>1:
#     print("I'm Sorry Hansoo")
# else:
#     print(alpha+odd_alpha+alpha[::-1])


##다시 풀어보기
string = list(input())
string.sort()

alpha_list = [0] * 26

for i in string: #A : 65 
    alpha_list[ord(i)-65] += 1

odd_cnt = 0

odd_alpha = ""
alpha = ""

for i in range(26):
    if alpha_list[i] % 2 == 1:
        odd_cnt += 1
        odd_alpha += (chr(i+65))
    alpha += chr(i+65) * (alpha_list[i] // 2)
    
if odd_cnt > 1:
    print("I'm Sorry Hansoo")
else:
    print(alpha + odd_alpha + alpha[::-1])


##다시 풀어보기
string = list(input())

alpha = [0] * 26

string.sort() #문자열 오름차순으로 정렬

for i in range(len(string)):
    alpha[ord(string[i])-65] += 1 #알파벳 개수를 저장 

odd_cnt = 0
odd_string = ""
total_string = ""
for i in range(len(alpha)):
    if alpha[i] % 2 == 1: #문자열의 알파벳 개수가 홀수라면, 
        odd_cnt += 1 #홀수 카운트 + 1 
        odd_string += chr(i+65) #홀수인 알파벳 저장 (홀수개인 알파벳이 가운데에 위치해야 하므로) 
    total_string += (alpha[i] // 2) * chr(i+65) #전체 알파벳을 절반 개수만 저장 (홀수개인 알파벳도 포함) 
    #예를들어 AAABB의 경우, odd_string 에 A 저장되고
    #                   total_string에 AB가 저장됨

if odd_cnt <= 1: #홀수개인 알파벳의 개수가 1보다 작거나 같으면 팰린드롬 가능   
    print(total_string + odd_string + total_string[::-1])
else:
    print("I'm Sorry Hansoo")


