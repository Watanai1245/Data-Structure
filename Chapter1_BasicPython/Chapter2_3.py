class TorKham:

	def __init__(self):
		self.lists = []

	def restart(self):
		self.lists.clear()
		return "game restarted"

	def play(self, sed):
            if(len(self.lists) == 0) :
                self.lists.append(sed[1])
                return self.lists
            else :    
                nsed = list(sed[1].lower())
                nlist = list(str(self.lists[-1]).lower())
                if(nsed[0] == nlist[-2] and nsed[1] == nlist[-1]) :
                    self.lists.append(sed[1])
                    return self.lists
                else :
                    return "game over"


t = TorKham()

print("*** TorKham HanSaa ***")
s = input("Enter Input : ").split(',')

sed = []
for i in range(0,len(s)) :
    sed = s[i].split()

    if (sed[0] == 'P') :
        print("'" + sed[1] + "'" + " ->",t.play(sed))
 
    elif (sed[0] == 'R'):
        print(t.restart())

    elif(sed[0] == 'X'):
        print(exit(0))
    
    else :
        print("'"+ s[i] +"' "+ "is Invalid Input !!!")
        print(exit(0))


