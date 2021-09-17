def hbd(age):
    if(age%2 == 0):
        return "saimai is just {}, in base {}!".format(20,age//2)
    else:
        return "saimai is just {}, in base {}!".format(21,age//2)
year = input("Enter year : ")
print(hbd(int(year)))