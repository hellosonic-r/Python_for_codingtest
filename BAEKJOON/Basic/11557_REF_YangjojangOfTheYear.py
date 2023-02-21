###딕셔너리로 풀어보기 

t = int(input()) #테스트 케이스 개수

for i in range(t):
    school = {} #딕셔너리 선언
    n = int(input()) #학교의 수
    for j in range(n):
        a, b = input().split()
        school[a]=int(b) #딕셔너리 {'키':'값'} 형태 / 값은 정수화 시켜야하므로 int로 감싼다.
    swap_school = dict(zip(school.values(),school.keys())) #school의 키,값 위치를 바꾸고 zip 함수로 묶고 dict로 저장한다.
    print(swap_school[max(swap_school)]) #딕셔너리[키]를 호출하면 값이 호출된다. 
                                         