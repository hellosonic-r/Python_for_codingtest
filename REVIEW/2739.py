###구구단
n = int(input())
def gugu(x,y):
    if y == 10:
        return
    print("{0} * {1} = {2}".format(x,y,x*y))
    gugu(x,y+1)
    
gugu(n,1)