# 1번 풀이
# s = list(input())

# i = 0
# start = 0
# while i < len(s):
#     if s[i] == "<":
#         i+=1
#         while s[i] != ">":
#             i+=1
#         i+=1
#     elif s[i].isalnum():
#         start = i
#         while i < len(s) and s[i].isalnum():
#             i+=1
#         temp = s[start:i]
#         temp.reverse()
#         s[start:i] = temp
#     else:
#         i+=1

# for j in range(len(s)):
#     print(s[j],end="")
#     if j == len(s)-1:
#         print()

# ##혹은
# #print("".join(s))

import sys

string = sys.stdin.readline().rstrip()
tag = False
ans = ""
stack = ""
for s in string:
    if s == "<":
        #원래대로 출력
        tag = True
        ans += stack[::-1]
        stack = ""
        ans += s
        continue
    elif s == ">":
        tag = False
        ans += s
        continue
    elif s == " ":
        ans += stack[::-1] + " "
        stack = ""
        continue

    if tag:
        ans += s
    else:
        stack += s
print(ans + stack[::-1])

# # 내 풀이    
# #띄어쓰기 만나면 출력 / < 만나면 출력 / > 만나면 출력

# string = list(input())
# string += " "
# ans = []

# #<>안의 띄어쓰기인지 체크하기 위함
# #-1 : <> 밖의 띄어쓰기, 1 : <> 안의 띄어쓰기
# check = -1

# for i in range(len(string)):
#     #띄어쓰기를 만나면
#     if string[i] == " ":
#         #만약 <>안의 띄어쓰기가 아니면
#         if check == -1:
#             #ans안의 요소들을 역순으로 출력
#             while ans:
#                 print(ans.pop(),end="")
#             #현재 글자(string[i]:띄어쓰기)는 출력이 안되었으므로
#             #따로출력
#             print(" ",end="")
#         #만약 <>안의 띄어쓰기라면
#         else:
#             #그냥 ans에 현재 글자(띄어쓰기)를 저장
#             ans.append(string[i])
#     #만약 < 를 만나면
#     elif string[i] == "<":
#         #우선 이제 만나는 띄어쓰기는 그냥 단순 ans에 저장
#         check = 1
#         #< 는 여태까지 저장된 ans를 역순으로 출력해주는 역할도 함
#         while ans:
#             print(ans.pop(),end="")
#         #ans를 다 비우고 ans에 다시 < 를 저장
#         ans.append(string[i])
#     #만약 > 를 만나면
#     elif string[i] == ">":
#         #현재 저장된 ans를 출력
#         for j in range(len(ans)):
#             print(ans[j],end="")
#         #ans를 다 출력했으니 초기화
#         ans.clear()
#         #현재 글자 (>)는 저장이 안되어있으므로 따로 출력
#         print(string[i],end="")
#         #<>를 탈출 했으므로 -1 저장(이제부터 만나는 띄어쓰기는 역순으로 출력하는 역할)
#         check = -1
#     #띄어쓰기, <, >를 제외한 글자를 만나면 단순 ans에 저장을한다
#     else:
#         ans.append(string[i])
# print()
        

        

    



        




