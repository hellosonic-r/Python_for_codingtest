for i in range(4):
    x1,y1,p1,q1,x2,y2,p2,q2 = map(int, input().split())
    if  x1 > p2 or p1 < x2 or y2 > q1 or q2
        print("d")
    elif x1 == p2 or p1 == x2:
        if q1 == y2 or y1 == q2:
            print("c")
        else:
            print("b")
    elif y2 == q1 or y1 == q2:
        print("b")
    else:
        print("a")