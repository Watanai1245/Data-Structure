input = list(input("Enter secret code : "))
print(input)
for i in range(len(input)-1):
    if input[i] == input[i+1]:
        print((ord(input[i])-96)*4)
        break