###OX퀴즈
import sys

t = int(input())
for i in range(t):
    quiz = list(map(str, sys.stdin.readline()))

    result = 0
    score = 0
    for j in range(len(quiz)):
        if quiz[j] == "O":
            score += 1
            result += score
        else:
            score = 0
    print(result)
