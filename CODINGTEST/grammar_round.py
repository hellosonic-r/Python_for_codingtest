#반올림, 올림, 내림, 버림
#올림, 내림, 버림 은 math 모듈 사용 (올림 : ceil / 내림 : floor / 버림 :trunc)
#반올림은 파이썬에 내장된 round 함수 사용

import math

#올림
print(math.ceil(-3.14)) # -3
print(math.ceil(3.14)) # 4

#내림
print(math.floor(-3.14)) # -4
print(math.floor(3.14)) # 3

#버림
print(math.trunc(-3.14)) # -3
print(math.trunc(3.14)) #3

#반올림
#math.round(숫자, 계산할자리수)
print(round(3.1415, 2)) # 3.14
print(round(5.88, 1)) # 5.9

##반올림 round함수의 사사오입 원칙
#반올림 하려는 자리수의 앞자리가 짝수이게끔 반올림
#중간 값인 2.5, 1.5 등은 짝수인 정수로 반올림
print(round(4.5)) # 4
print(round(3.5)) # 4