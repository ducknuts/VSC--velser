
def echo(streng):
    if len(streng) > 2:
        for x in range(3):
            print(streng[:3], end = "")
    else: 
        for x in range(3):
            print(streng, end = "")

echo(input("Indtast et ord: "))

