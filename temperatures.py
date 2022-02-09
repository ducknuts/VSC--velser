cel_temp = 0
fahr_temp = 0

def cel2fahr(cel_temp):
    return cel_temp * (9/5) + 32

print(cel2fahr(int(input("Indtast celcius, og jeg konverterer til fahrenheit: "))))


def fahr2cel(fahr_temp):
    return (fahr_temp - 32) * 5/9

print(fahr2cel(int(input("Indtast fahrenheit, og jeg konverterer til celcius: "))))

