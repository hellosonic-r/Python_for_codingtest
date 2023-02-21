# A : 5분
# B : 1분
# C : 10초

T = int(input())  ## 500
A, B, C = 300, 60, 10

fin_A = 0 #1
fin_B = 0 #3
fin_C = 0 #2

if T % 10 != 0:
    print(-1)
else:
    fin_A = T // A
    fin_B = T % A // B
    fin_C = T % A % B // C
    print(fin_A,fin_B,fin_C)
        

