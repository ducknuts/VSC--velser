decimal = int(input("Indtast en decimal: "))
hex_list = []
hex_dict = {
    0: "0",
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F",
}

while decimal > 0:
    rest_convert = decimal % 16
    decimal = decimal // 16
    if rest_convert in hex_dict.keys():
        hex_list = hex_list + [hex_dict[rest_convert]]

for i in hex_list[::-1]:
    print(i, end = "")



