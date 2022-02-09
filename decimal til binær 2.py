decimal = int(input("Indtast et helt tal: "))
remainder_list = []
i = 0

while decimal != 0:
    remain = decimal % 2
    remainder_list.insert(i, remain)
    i = i + 1
    decimal = int(decimal / 2)

i = i - 1
print("\nEquivalent Binary Value is:")
while i >= 0:
    print(end = str(remainder_list[i]))
    i = i - 1

