def move(n,A,B,C):
    if n > 0:
        move(n-1,A,C,B)
        l[C-1].append(l[A-1].pop())
        print("move",n,"from ", chr(ord('A')+A-1), "to", chr(ord('A')+C-1))
        print("|  |  |")
        printall(l[0], l[1], l[2], size)
        move(n-1,B,A,C)
def printall(a,b,c,x):
    if x == 0:
        return
    else:
        if len(a)>=x:
            print(a[x-1], end='  ')
        else:
            print("| ", end=' ')
        if len(b)>=x:
            print(b[x-1], end='  ')
        else:
            print("| ", end=' ')
        if len(c)>=x:
            print(c[x-1], end='  ')
        else:
            print("| ", end=' ')
        print()
        printall(a,b,c,x-1)
def init(n):
    if n == 0:
        return []
    return [n] + init(n-1)
size = int(input("Enter Input : "))
l = [[]]*3
l[0] = init(size)
l[1] = list()
l[2] = list()
print("|  |  |")
printall(l[0],l[1],l[2],size)
move(size,1,2,3)