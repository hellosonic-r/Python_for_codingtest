a, b = map(int, input().split()) # 24 18 입력
a_divisor = 2
b_divisor = 2
a_cd = [1]
b_cd = [1] #약수 리스트
while a_divisor != a+1 :
    if a % a_divisor == 0:
        a_cd.append(a_divisor)
        a_divisor += 1
    else:
        a_divisor += 1

while b_divisor != b+1 :
    if b % b_divisor == 0:
        b_cd.append(b_divisor)
        b_divisor += 1
    else:
        b_divisor += 1

cd = []

for i in range(len(a_cd)):
    for j in range(len(b_cd)):
        if a_cd[i] == b_cd[j]:
            cd.append(a_cd[i])
gcd = max(cd) #최대공약수
print(gcd) #최대공약수
print(gcd*(a//gcd)*(b//gcd)) #최소공배수