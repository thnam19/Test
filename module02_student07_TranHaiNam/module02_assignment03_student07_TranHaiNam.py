

a=str(input(" Tên học viên:"))
b=int(input(" id học viên:"))
c=int(input(" Số thứ tự tuần học:"))
d=int(input(" Số thứ tự bài tập:"))

def file(a,b,c,d):
    a1=a.replace(" ","")
    print(f"week{c:02}_assignment{d:02}_student{b:02}_{a1}.py")
file(a,b,c,d)
    
