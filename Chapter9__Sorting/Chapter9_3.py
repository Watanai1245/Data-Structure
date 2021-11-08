def drome(lst):
    des = True
    asc = True
    unique = True
    same = True
    List = []
    for i in range(len(lst)-1):
        if lst[i] < lst[i+1]:
            des = False
        if lst[i] > lst[i+1]:
            asc = False
        if lst[i] in List:
            unique = False
        if lst[i] != lst[i+1]:
            same = False
        List.append(lst[i])

    if lst[len(lst)-1] in List:
        unique = False

    if same:
        return "Repdrome"
    elif asc and unique:
        return "Metadrome"
    elif asc and not unique:
        return "Plaindrome"
    elif des and unique:
        return "Katadrome"
    elif des and not unique:
        return "Nialpdrome"
    else:
        return "Nondrome"

def test():
    test_lst = [("1357","Metadrome"), ("12344","Plaindrome"), ("7531","Katadrome"), ("9874441","Nialpdrome"), ("666","Repdrome"), ("1985","Nondrome")]
    for item in test_lst:
        res = drome(list(item[0]))
        if res != item[1]:
            print(f"Case {item[0]} failed: {res} != {item[1]}")
        else:
            print(f"Case {item[0]} success")

if __name__ == '__main__':
    in_lst = list(map(int, input("Enter Input : ")))
    print(drome(in_lst))