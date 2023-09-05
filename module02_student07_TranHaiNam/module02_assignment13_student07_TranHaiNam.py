str1= "áàảãạăắằẳẵặâấầẩẫậéèẻẽẹêếềểễệóòỏõọôốồổỗộơớờởỡợíìỉĩịúùủũụưứừửữựýỳỷỹỵDĐ"
str2= "aaaaaaaaaaaaaaaaaeeeeeeeeeeeoooooooooooooooooiiiiiuuuuuuuuuuuyyyyyDD"

province=input(str("Nhập tên tỉnh hoặc thành phố:"))

def main(province):
    province1= ""
    for char in province:
        if " " in char:
            province.replace(" ","")
        elif char in str1:
            province1 += str2[str1.find(char)]
        else:
            province1 += char
    print(province1)
main(province)


