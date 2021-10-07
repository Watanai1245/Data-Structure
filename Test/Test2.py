print(" *** Divisible number ***")
list1 = []
num = int(input("Enter a positive number : "))
if(num == 0):
    print("0 is OUT of range !!!")
    
else:
    for i in range (1,num+1):
        if(num % i == 0):
            list1.append(i)
    print("Output ==>", end =' ')
    for i in list1:
        print(i, end =" ")
    print("\nTotal ==>", len(list1))