print("*** Election ***")
voter = int(input("Enter a number of voter(s) : "))
if(voter<=0):
    print("*** No Candidate Wins ***")
    exit()
numList = [int(e) for e in input().split()]
false = 0
for i in numList:
    if(  i <= 0 or i >20 ):
        numList.remove(i)
newList = []
newList = numList.copy()

newList.remove(max(set(numList),key=numList.count))
if (numList == [] or newList == []):
    print("*** No Candidate Wins ***")
elif(newList.count(max(set(newList),key=newList.count)) == numList.count(max(set(numList),key=numList.count))):
        print("*** No Candidate Wins ***")
else:
    print(max(set(numList),key=numList.count))