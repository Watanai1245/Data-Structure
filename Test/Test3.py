print(" *** Recite the multiplication table ***")
inp = input("Enter pattern for child 1 to 3 (-1 for sep) : ").split("-1")

a = list(map(int, inp[0].split()))
b = list(map(int, inp[1].split()))
c = list(map(int, inp[2].split()))
Child1 = [-1, 0, len(a)]
Child2 = [-2, 0, len(b)]
Child3 = [-3, 0, len(c)]
count = 0
check = True

while True:
    if Child1[1] == Child1[2]:
        Child1[1] = 0
    if Child2[1] == Child2[2]:
        Child2[1] = 0
    if Child3[1] == Child3[2]:
        Child3[1] = 0
    count += 1
    Child1[0], Child2[0], Child3[0] = a[Child1[1]], b[Child2[1]], c[Child3[1]]
    if Child1[0] == Child2[0] == Child3[0]:
        break
    Child1[1] += 1
    Child2[1] += 1
    Child3[1] += 1
    if count > 365:
        check = False
        break

a = list(map(str, inp[0].split()))
b = list(map(str, inp[1].split()))
c = list(map(str, inp[2].split()))

aa = " ".join(a)
bb = " ".join(b)
cc = " ".join(c)

print("    ")
print(f"Pattern for child 1 : {aa}")
print(f"Pattern for child 2 : {bb}")
print(f"Pattern for child 3 : {cc}")

if check:
    print(f"They recite same multiplication table in {count} days")
else:
    print("This year they never recite same multiplication table !!!")