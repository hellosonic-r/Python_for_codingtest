def recursiveFunction(i):
    #10번째 출력했을 때 종료되도록 종료 조건 명시
    if i == 5 :
        return
    print(i, "번째 재귀 함수에서", i+1, "번째 재귀 함수를 호출합니다.")
    recursiveFunction(i+1)
    print(i, "번째 재귀 함수를 종료합니다.")

recursiveFunction(1)