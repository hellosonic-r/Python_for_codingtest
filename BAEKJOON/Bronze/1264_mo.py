while True:
    string_list = list(input())
    if string_list == ["#"]:
        break
    m = ["a","e","i","o","u","A","E","I","O","U"]
    cnt = 0
    for i in string_list:
        if i in m:
            cnt += 1
    print(cnt)