Liat = [int(i) for i in input('Enter Input : ').split()]

for loop in range(1, len(Liat)):
    moveNum = None 
    swap = False 
    for i in range(len(Liat) - loop):  
        if Liat[i] > Liat[i + 1]:    
            moveNum = Liat[i]  
            Liat[i], Liat[i + 1] = Liat[i + 1], Liat[i]  
            swap = True                               

    if loop <= len(Liat) - 1 and swap is False:       
        print('last step :', Liat, f'move[{moveNum}]')  
        break
    elif loop == len(Liat) - 1:    
        print('last step :', Liat, f'move[{moveNum}]')
    else:                                              
        print(f'{loop} step :', Liat, f'move[{moveNum}]')