#datetime 모듈
from datetime import datetime, timedelta

time1 = datetime(2022, 1, 9 ,10, 26, 35, 5)
time2 = datetime.now() #현재시각
print(time1)

print("두 날짜의 차 구하기") #timedelta
print((time2-time1).days ,"일") ###print 함수 내의 값을 연결 시킬때 <,> 혹은 <+> 사용
print((time2-time1).seconds ,"초") ###<,>는 모든 자료형의 값 연결 가능 / <+>는 문자열만 연결 가능
print((time2-time1).seconds / 3600 ,"시간")

print("현재시각으로부터 5일 뒤")
print(time2 + timedelta(days=5))

###날짜만 구하기
today = datetime.today()
print(today.date())