T = int(input())

for i in range(T): #T는 불변 i가 변한다
    A, B = map(int, input().split())
    print("Case #"+str(i+1)+":",A+B) #T가 아니라 i 넣기
