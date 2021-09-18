'''
\n => การขึ้นบรรทัดใหม่
\t => การเว้น 1 แท็ป
'''
#
#
#
#
#
### คำสั่งที่ใช้สำหรับแสดงผล
print("คำสั่งที่ใช้สำหรับแสดงผล")

print("Hello World 1") 
print('Hello World 2') #string => ข้อความ ตัวอักษร

print(-1) 
print(0) 
print(1) 
print(1+2+3+4+5) #int => จำนวนเต็ม 

print(True)
print(False) #Boolean => 2 เงื่อนไข ตัวแรกต้องเป็นพิมใหญ่
print('\n')
#
#
#
#
#
### Data Type & Variable
print("Data Type & Variable")
x = 20 # integar
y = 3.99
z = True
print('ผลลัพธ์ = ' + str(x))
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z)) #การแสดงผลชนิดตัวแปร
print('\n')
#
#
#
#
#
### การรับค่าจากแป้นพิมพ์
#*** input() #จะรับค่าเป็น str
#print('\n')
#
#
#
#
#
### การดำเนินการทางคณิตศาสตร์
print("การดำเนินการทางคณิตศาสตร์")
'''
+  ->  บวก
-  ->  ลบ 
*  ->  คูณ
/  ->  หาร
// ->  หารปัดเศษ เช่น 14 / 10 = 1
** ->  ยกกำลัง เช่น 5**2 = 5 ยกกำลัง 2 = 25
%  ->  หารเอาเศษ เช่น 14 % 10 = 2

''' 
print('\n')
#
#
#
#
#
### ตัวดำเนินการเปรียบเทียบ
print("ตัวดำเนินการเปรียบเทียบ")
'''
>  ->  มากกว่า #โปรแกรมจะตอบตำตอบออกมาในรูปแบบของ Boolean
<  ->  น้อยกว่า
>= ->  มากกว่าหรือเท่ากับ
<= ->  น้อยกว่าหรือเท่ากับ
== ->  เท่ากับ
!= ->  ไม่เท่ากับ
and และ
or  หรือ
not นิเสธ(ใส่หน้าตัวแปรที่ต้องการทำเป็นนิเสธ)
'''
print('\n')
#
#
#
#
#
### เงื่อนไข การเขียน if...else
print("ตัวดำเนินการเปรียบเทียบ")
abc = 1 
if (abc > 0) :
    print("มากกว่า 0")
elif abc < 0 :
    print("น้อยกว่า 0")
else :
    print("เท่ากับ 0")   
print('\n')
#
#
#
#
#
### Ternary Operator
print("ตัวดำเนินการเปรียบเทียบ")
print("123") if abc >= 1 else print("456") #การลดรูปของ if...else ให้สั้นลง
print('\n')
#
#
#
#
#
### String 

name = "newyear watanai  " #index
print(name[2]) #คือการแสดงผลตัวอักษรตัวแรก คือ "n"
print(name[2:5]) #คือการแสดงผลตัวอักษรลำดับที่ 0-4 คือ "newye"
print(len(name)) #คือการแสดงความยางททั้งหมดของ String รวมถึง 'ช่องว่าง'
print(name.upper()) #คือการแปลงตัวอักษรจากตัวเล็กให้กลายเป็นตัวพิมใหญ่ทั้งหมด
print(name.lower()) #คือการแปลงตัวอักษรจากตัวใหญ่ให้กลายเป็นตัวพิมเล็กทั้งหมด
print(name.capitalize()) #คือการแปลงตัวอักษรให้ตัวแรกเป็นตัวพิมใหญ่เพียงตัวเดียว
print(name.replace("new","123")) #การแทนที่ตัวอักษรตัวเดิม ตัวแรกที่ใส่จะเป็นตัวอักษรตัวเดิมที่เราต้องการให้เปลี่ยน ส่วนตัวหลังนั้้นจะเป็นตัวอักษรใหม่ที่เราต้องการให้มันเข้าไปแทนที่
print(name.replace("new","123",1)) #เลข 1 ข้างหลังคอสมมติว่าเรามี " new " หลายตัวโปรแกรมก็จะเลือกเปลี่่ยน 1 ตัว
name1 = name.strip() #คือการตัด'ช่องว่าง'ทั้งซ้ายและขวาออก
name2 = name.lstrip() #คือการตัด'ช่องว่าง'ทางซ้ายออก
name3 = name.rstrip() #คือการตัด'ช่องว่าง'ทางขวาออก
# x = "new" in name คืือคำสั่งที่ใช้บอกว่า มีคาว่า " new" อยู่ในตัวแปร name มั้ย

A = "new"
B = "year"
C = 20
text = "ชื่อ : {} \tนามสกุล : {} \t อายุ : {}"
print(text.format(A,B,C))