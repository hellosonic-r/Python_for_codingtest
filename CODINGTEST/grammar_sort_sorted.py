###sort 와 sorted의 차이
##ed 가 붙으면 원본 그대로
#sort 함수
a1 = [6, 3, 9]
print("a1 :",a1)
a2 = a1.sort()
print("---정렬후---")
print("a1 :",a1) #[3,6,9]
print("a2 :",a2) #None >> 단순히 정렬만 하고 값이 리턴되지 않는다.

#sorted 함수
b1 = [6, 3, 9]
print("b1 :",b1)
b2 = sorted(b1)
print("---정렬후---")
print("b1 :",b1) #[6,3,9]
print("b2 :",b2) #[3,6,9]

#reverse 함수 : 순서 뒤집기
c1 = [6, 3, 9]
print("c1 :",c1)
c2 = c1.reverse()
print("---정렬후---")
print("c1 :",c1) #[9,3,6]
print("c2 :",c2) #None