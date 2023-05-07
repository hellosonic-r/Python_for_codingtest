##나의 코드
for test_case in range(1,11):
    n = int(input()) #원본 암호문의 길이
    num_list = list(map(int, input().split())) #원본 암호문 
    command = int(input()) #명령어의 개수
    command_list = list(map(str, input().split()))
    insert_cnt = 0 #명령어 개수 카운트하기 위한 변수
    for i in range(len(command_list)): 
        if command_list[i] == "I": #만약 I를 만나면
            insert_cnt += 1 #일단 명령어 개수 카운트 (command 변수와 같아지면 반복문 탈출)
            idx = 0 #insert 메서드 파라미터 중 위치에 해당하는 파라미터에 들어갈 인덱스를 더해줘야 함
            #ex) [0,1,2,3]의 1번 인덱스에 ex = [-1,-1]를 넣는다면
            #   1) insert(1, ex[0]) --> [0,-1,1,2,3]
            #   2) 1)의 결과에서 2번 인덱스에 ex[1] = -1이 들어가야 함 
            #   3) insert(2, ex[1]) --> [0,-1,-1,1,2,3]      
            for j in range(i+3,i+3+int(command_list[i+2])): #숫자들을 삽입하기 위해 반복문 수행
                num_list.insert(int(command_list[i+1])+idx, int(command_list[j]))
                idx+=1
        if insert_cnt == command:
            break
    ans_list = num_list[:10]
    print("#{} {}".format(test_case, " ".join(map(str, ans_list))))


##다른 코드
for test_case in range(10):
    n = int(input())
    num_list = list(map(int, input().split()))
    command = int(input())
    command_list = list(map(str, input().split()))
    for i in range(len(command_list)):
        if command_list[i] == "I":
            idx = int(command_list[i+1]) #idx와
            nums = int(command_list[i+2]) #뒤에 올 숫자들을 미리 변수에 저장해두고 아래의 for문에서 활용
            for j in range(nums):
                command_list.insert(idx+j, int(command_list[i+2+(j+1)]))
        else:
            continue
    print("#{} {}".format(test_case, " ".join(map(str, command_list[:10])))) #정답에 직접 슬라이싱


