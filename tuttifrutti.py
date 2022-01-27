print('Apples: 5.00 kr.')
print('Pears: 4.00 kr.')
print('Bananas: 6.00 kr.')
print('Pineapples: 20.00 kr.')

print('Delivery charge: 32.50 kr.')
apples = int(input('How many apples? '))
pears = int(input('How many pears?'))
bananas = int(input('How many bananas?'))
pineapples = int(input('How many pineapples?'))

total = (apples * 5) + (pears * 4) + (bananas * 6) + (pineapples * 20)
total = total + 32.50
print(f'To be payed in full: {total} kr.')