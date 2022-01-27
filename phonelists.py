# numre = [0, 1, 2, 3]
# navne = ["Olaf", "Peter", "Lars", "John"]
telefonnumre = ["12345678", "00000000", "87654321", "24681012"]


print("Der er følgende personer i telefonlisten. Indtast nummeret svarende til personen, og få vedkommendes telefonnummer!")
print("Olaf: 0")
print("Peter: 1")
print("Lars: 2")
print("John: 3")

user_input = int(input("Indtast nummeret: "))

if user_input == 0:
    print(telefonnumre[0])
elif user_input == 1:
        print(telefonnumre[1])
elif user_input == 2:
    print(telefonnumre[2])
else:    
    print(telefonnumre[3])