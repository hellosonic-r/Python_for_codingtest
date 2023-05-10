n = int(input())

for _ in range(n):
    string = list(input())
    score_sum = 0
    score = 0
    for i in range(len(string)):
        if string[i] == "O":
            score += 1
            score_sum += score
        elif string[i] == "X":
            score = 0
    print(score_sum)