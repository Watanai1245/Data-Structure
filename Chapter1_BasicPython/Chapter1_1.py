print("*** Rabbit & Turtle ***")
d,vr,vt,vf = input("Enter Input : ").split()
D = int(d)
Vr = int(vr)
Vt = int(vt)
Vf = int(vf)
total = (D/(Vt-Vr))*Vf
print('%.2f' %total)

