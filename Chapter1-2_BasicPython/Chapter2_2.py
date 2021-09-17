def weirdSubtract(n,k):
    for i in range(0,k) :        
        scrap = n % 10
        if (scrap == 0):
            n =  n / 10
        elif ( scrap > 0) :
            n = n - 1
    return int(n)

a,b = input("Enter num and sub : ").split()
print(weirdSubtract(int(a),int(b)))