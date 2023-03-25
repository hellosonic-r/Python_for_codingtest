from collections import deque
n = int(input())

for _ in range(n):
    page ,sequence = map(int,input().split())
    queue = deque(map(int, input().split()))

    #구하려고 하는 인덱스(pop() 메서드 따라 구하려는 인덱스도 변동되어야한다.)
    ans_idx = sequence 
    #몇 번째로 출력하는지 세기 위한 변수
    time = 1 
    while True:
        #현재 큐 중 우선순위가 가장 큰 인덱스를 구한다.
        max_idx = queue.index(max(queue)) # 3 # 2
        #우선순위가 가장 큰 인덱스의 이전 인덱스까지 popleft()를 통해 뒤에다 붙인다.
        # [1,2,3,4] -> [4,1,2,3]
        for _ in range(max_idx):
            queue.append(queue.popleft())
        #popleft()를 통해 요소의 위치가 변화가 일어남에 따라, 
        #원래 찾으려는 인덱스는 어디에 있는지 찾는다.
        ans_idx = (ans_idx + len(queue) - max_idx) % len(queue)
        #만약 찾으려는 인덱스의 위치가 현재 idx 0 에 있다면, 맨 앞에 있는 것이고
        #출력 순서가 된 것이므로 time을 출력하고 반복문을 탈출한다.
        if ans_idx == 0:
            print(time)
            break
        #찾으려는 인덱스의 위치가 idx 0 이 아니라면,
        else:
            #맨 앞에 있는(우선순위가 가장 높은) 프린트를 출력하고
            queue.popleft()
            #앞의 프린트가 출력이 되었으므로, 찾으려는 인덱스 위치는 한 칸 앞으로 간다.
            ans_idx -= 1
            #출력이 되었으므로 출력 횟수를 표시하는 변수인 time에 1을 더해준다.
            time+=1
    
