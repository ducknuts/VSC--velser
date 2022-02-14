dec_convert = int(input("Indtast et decimaltal: "))
new_list = []
while dec_convert > 0:
    rest_convert = dec_convert % 2
    dec_convert = dec_convert // 2
    
    new_list = new_list + [rest_convert]

print(new_list)
print(new_list[::-1])



