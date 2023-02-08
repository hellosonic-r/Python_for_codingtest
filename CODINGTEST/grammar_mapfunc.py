#how to use map func

#map 은 리스트의 요소를 지정된 함수로 처리해주는 함수
#list(map(함수, 리스트))
#input() : 입력 함수 
#split() : 입력값을 구분하는 함수

#for 문 사용
a = [1.2, 3.4, 5.6, 7.8]
for i in range(len(a)):
    a[i] = int(a[i]) # 가져온 인덱스로 요소 하나하나에 접근하고 int 로 변환

print(a)

#map 함수 사용
b = [1.2, 3.4, 5.6, 7.8]
b = list(map(int, b))
print(b)

#map(int, input().split())
c = map(int, input().split())
print(list(c))
