string = input()

board = [0] * 26

for i in string:
    board[ord(i) - 97] += 1

print(" ".join(map(str, board)))