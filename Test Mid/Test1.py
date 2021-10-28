list1 = []
sum = 0
print(" *** Multiples of 3 or 5 or 7 ***")
num = int(input("Enter number : "))
if(num < 0):
    print("Only positive number !!!")
else:
    for i in range (1,num):
        if(i % 3 == 0 or i % 5 == 0 or i % 7 == 0):
            list1.append(i)
    for i in list1:
        sum += i

    print("Result :" ,sum)

