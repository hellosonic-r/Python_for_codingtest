###sort 와 sorted의 차이

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