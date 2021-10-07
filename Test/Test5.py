class MyInt:
    def __init__(self,list = None):
        if list == None:
            self.word = []
        else:
            self.word = list

    def deciToRoman(self, num):
        uint = num % 10
        ten = int(((num % 100)-uint)/10)
        hundreds = int(((num % 1000)-(ten+uint))/100)
        thousands = int((num % 10000-(hundreds+ten+uint))/1000)

        roman = {1: 'I', 5: 'V', 10: 'X', 50: 'L',
                 100: 'C', 500: 'D', 1000: 'M', 5000: 'MMMMM'}
        listn = ""

        if thousands <= 3:
            listn += (roman[1000]*thousands)
        elif thousands == 4:
            listn += (roman[1000]+roman[5000])
        elif 5 <= thousands <= 8:
            listn += (roman[5000]+roman[1000]*(thousands-5))
        elif thousands == 9:
            listn += (roman[1000]+roman[10000])

        if hundreds <= 3:
            listn += (roman[100]*hundreds)
        elif hundreds == 4:
            listn += (roman[100]+roman[500])
        elif 5 <= hundreds <= 8:
            listn += (roman[500]+roman[100]*(hundreds-5))
        elif hundreds == 9:
            listn += (roman[100]+roman[1000])

        if ten <= 3:
            listn += (roman[10]*ten)
        elif ten == 4:
            listn += (roman[10]+roman[50])
        elif 5 <= ten <= 8:
            listn += (roman[50]+roman[10]*(ten-5))
        elif ten == 9:
            listn += (roman[10]+roman[100])

        if uint <= 3:
            listn += (roman[1]*uint)
        elif uint == 4:
            listn += (roman[1]+roman[5])
        elif 5 <= uint <= 8:
            listn += (roman[5]+roman[1]*(uint-5))
        elif uint == 9:
            listn += (roman[1]+roman[10])

        return listn

    def __add__(self,num1,num2):
        a = (num1+num2)+((num1+num2)/2)
        return a

print(" *** class MyInt ***")
num1,num2 = input("Enter 2 number : ").split()
n1 = int(num1)
n2 = int(num2)
print(n1 ,"convert to Roman :" ,MyInt().deciToRoman(n1))
print(n2 ,"convert to Roman :" ,MyInt().deciToRoman(n2))
print(n1 ,"+", n2,"=",'%.0f' % MyInt().__add__(n1,n2))
