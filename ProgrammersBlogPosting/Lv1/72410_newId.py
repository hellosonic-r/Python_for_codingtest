def solution(new_id):
    answer = ''
    
    #1단계
    new_id = new_id.lower() 
    new_id_list = list(map(str, str(new_id)))
    new_id = ''
    print("1단계:","".join(map(str,new_id_list)))
    
    #2단계
    for i in range(len(new_id_list)):
        if 97<=ord(new_id_list[i])<=122 or 48<=ord(new_id_list[i])<=57 \
        or new_id_list[i] in ["-", "_", "."]:
            new_id += new_id_list[i]
    print("2단계:",new_id)
    
    #3단계
    condot = ''
    for i in range(len(new_id), 1, -1):
        condot = '.' * i
        new_id = "".join(map(str, new_id.replace(condot,".")))
    print("3단계:",new_id)
    
    #4단계
    if new_id[0] == "." and new_id[-1] == ".":
        new_id = new_id[1:len(new_id)-1]
    elif new_id[0] == "." and new_id[-1] != ".":
        new_id = new_id[1:]
    elif new_id[0] != "." and new_id[-1] == ".":
        new_id = new_id[:len(new_id)-1]
    print("4단계:",new_id)
        
    #5단계
    if new_id == "":
        new_id = "a"
    print("5단계:",new_id)
        
    #6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == ".":
            new_id = new_id[:14]
    print("6단계:",new_id)
            
    #7단계
    if len(new_id) <= 2:
        x = new_id[-1]
        while True:
            new_id += x
            if len(new_id) == 3:
                break
    
    answer = new_id
    
    return answer