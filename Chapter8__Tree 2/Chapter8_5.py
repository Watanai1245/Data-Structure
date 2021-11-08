
def printTree(data, index, size, level):
    if  index < size:
        printTree(data, 2 * index + 2, size, level + 1)
        print('        ' * level, data[index])
        printTree(data, 2 * index + 1, size, level + 1)


if __name__ == '__main__':
    input = input('Enter Input : ').split('/')

    data = []
    van = {}

    for name in range(int(input[0])):
        van[name + 1] = van.get(name + 1, 0)
        data.append(int(name) + 1)

    for cus, key in enumerate(input[1].split()):
        print(f'Customer {cus + 1} Booking Van {data[0]} | {key} day(s)')
        temp = data.pop(0)
        van[temp] = van.get(temp, 0) + int(key)
        for index, key in enumerate(data):
            if  van[temp] < van[key] or (van[temp] == van[key] and temp < key):
                data.insert(index, temp)
                temp = None
                break
        if temp:
            data.append(temp)