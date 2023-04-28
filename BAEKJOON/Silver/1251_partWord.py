string = list(input())
length = len(string)
check = ["z"]*length #이렇게 해야지 초기 비교 시 무조건 뒤집은 값으로 갱신됨
for i in range(1,length-1):
    for j in range(i+1,length):
            if check > string[:i][::-1] + string[i:j][::-1] + string[j:][::-1]:
                  check = string[:i][::-1] + string[i:j][::-1] + string[j:][::-1]

print("".join(map(str,check)))
