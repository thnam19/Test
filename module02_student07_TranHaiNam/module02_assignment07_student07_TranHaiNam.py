alphabet = "abcdefghijklmnopqrstuvwxyz"
message = str(input(" Từ cần giải mã là: "))
key = 13
new_message= ""

def giai_ma(alphabet,message,key,new_message):
    for char in message:
        if char in alphabet:
            position = alphabet.find(char)
            new_position = (position + key) % 26
            new_char = alphabet[new_position]
            new_message += new_char
    print("mật mã đã giải là:"+new_message)
giai_ma(alphabet,message,key,new_message)


# Trường hợp mã hóa ta cần thay key= -13.




        