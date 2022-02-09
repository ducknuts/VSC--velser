def omregner(num):  
        if num >= 1:
            omregner(num // 2)
        print(num % 2, end = '')


while True:
    print('\n')
    num = int(input("Indtast et helt tal, og jeg omregner det til binær: "))
    omregner(num)

