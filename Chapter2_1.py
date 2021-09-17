class translator:

    def decToRoman(self, num):
        first = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX"}
        second = {1: "X", 2: "XX", 3: "XXX", 4: "XL", 5: "L", 6: "LX", 7: "LXX", 8: "LXXX", 9: "XC"}
        third = {1: "C", 2: "CC", 3: "CCC", 4: "CD", 5: "D", 6: "DC", 7: "DCC", 8: "DCCC", 9: "CM"}
        fourth = {1: "M", 2: "MM", 3: "MMM"}

        collec = ""
        temp = 0
        nlist = []
        roman = ""
        leng = len(str(num))

        for x in range(0, leng):
            temp = num % 10
            num = (num - temp) / 10
            nlist.append(int(temp))

        for y in range(0, leng):
            if y == 0:
                if nlist[y] in first:
                    nlist[y] = first[nlist[y]]
            elif y == 1:
                if nlist[y] in second:
                    nlist[y] = second[nlist[y]]
            elif y == 2:
                if nlist[y] in third:
                    nlist[y] = third[nlist[y]]
            elif y == 3:
                if nlist[y] in fourth:
                    nlist[y] = fourth[nlist[y]]
        nlist.reverse()

        for z in range(0,leng):
            roman += nlist[z]

        return roman

    def romanToDec(self, s):
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        i = 0
        num = 0
        while i < len(s):
            if i+1<len(s) and s[i:i+2] in roman:
                num+=roman[s[i:i+2]]
                i+=2
            else:
                #print(i)
                num+=roman[s[i]]
                i+=1
        return num


num = int(input("Enter number to translate : "))

r = translator().decToRoman(num)
d = translator().romanToDec(r)

print(r)
print(d)