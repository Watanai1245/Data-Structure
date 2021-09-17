def reverse(l):
    if len(l) == 0: 
        return []
    else : 
        return [l.pop()] + reverse(l)

def recursive_sum(lst):
    if not lst:
        return 0
    else:
        return int(lst[0]) + recursive_sum(lst[1:])

l = input("Enter your List : ").split(",")
A = reverse(l)
B = recursive_sum(A)
print("List after Sorted :",B)