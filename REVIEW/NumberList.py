##숫자의 각 자리수를 요소로 갖는 리스트로 변환
#1
a = input()
a_list = list(map(int, str(a)))
print(a_list)

#2
b_list = [int(b) for b in str(input())]
print(b_list)