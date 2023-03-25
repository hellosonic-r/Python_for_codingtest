# for문 사용

import sys
n = int(input())

for _ in range(n):
    string = list(sys.stdin.readline().rstrip())
    ans = [0]
    #만약 입력한 문자열에서 '('의 개수와 ')'의 개수가 다르다면 VPS가 아니다.
    if string.count("(") != string.count(")"):
        print("NO")
    #'('의 개수와 ')'의 개수가 같다면,
    else:
        #문자열의 맨 끝부터 확인한다.
        for i in range(len(string)-1, -1, -1):
            #문자가 ')'이라면
            if string[i] == ")":
                #문자열에서 해당 문자를 없애고
                string.pop()
                #ans에 0을 추가한다.
                ans.append(0)
            #문자가 '(' 이라면
            else:
                #ans중 가장 최근에 들어간 0을 제거한다.
                ans.pop()
            #이 때, 만약 ans가 비어있다면, ')'에 비해 '('가 더 많아져서 
            #VPS가 될 가능성이 없다.
            if len(ans) == 0:
                print("NO")
                break
            #만약 ans가 비어있지 않다면 계속해서 반복을 수행한다.
            else:
                continue
        #반복을 수행한 후 ans에 0 하나만 들어있다면 VPS이고, YES를 출력한다.
        if len(ans) == 1:
            print("YES")
        else:
            continue


#while문 사용

import sys
n = int(input())

for _ in range(n):
    string = list(sys.stdin.readline().rstrip())
    ans = [0]
    #만약 입력한 문자열에서 '('의 개수와 ')'의 개수가 다르다면 VPS가 아니다.
    if string.count("(") != string.count(")"):
        print("NO")
    #'('의 개수와 ')'의 개수가 같다면,
    else:
        #문자열 리스트가 빌 때까지 확인한다.
        while string:
            #x에 string 문자열의 마지막 문자를 제거하고 제거된 문자를 x에 저장한다
            x = string.pop()
            #제거된 문자가 ')'이라면
            if x == ")":
                #ans에 0을 추가한다.
                ans.append(0)
            #제거된 문자가 '(' 이라면
            else:
                #ans에 저장된 마지막 값을 하나 제거한다
                ans.pop()
            #이 때, 만약 ans가 비어있다면, ')'에 비해 '('가 더 많아져서 
            #VPS가 될 가능성이 없다.
            if len(ans) == 0:
                print("NO")
                break
            #만약 ans가 비어있지 않다면 계속해서 반복을 수행한다.
            else:
                continue

        #반복을 수행한 후 ans에 0 하나만 들어있다면 VPS이고, YES를 출력한다.
        if len(ans) == 1:
            print("YES")
        else:
            continue

##다른 사람 코드 단순 구현
import sys

n = int(input())
for _ in range(n):
    string = list(sys.stdin.readline().rstrip())
    sum = 0
    for i in string:
        if i == "(":
            sum += 1
        elif i == ")":
            sum -= 1
        if sum < 0:
            print("NO")
            break
    if sum > 0:
        print("NO")
    elif sum == 0:
        print("YES")

