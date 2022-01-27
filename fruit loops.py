goods = ['Apples', 'Pears', 'Bananas', 'Cherries', 'Pineapples', 'Plums', 'Dicks']
prices = [5, 4, 6, 20, 25, 3, 100]
count = [0, 0, 0, 0, 0, 0, 0] 
# Count var tom, og der er derfor ikke en index 'i', som count[i] beder om at placere brugerens input i. 
sum = 0
for i in range(0, 7):
    print(f'{goods[i]} is {prices[i]} kr.')
    print(f'How many {goods[i]} do you want : ')
    count[i] = int(input())
# Derudover forsøgte vi at lægge en integer sammen med en streng. 
# Strengen er i dette tilfælde et brugerinput, som vi caster til en integer med int()
    price = prices[i] * count[i]
    print(f'Cost: {price} kr.')
    sum = sum + price
price = 32.5
print(f'Delivery charge is {price} kr.')
sum = sum + price
print(f'Total : {sum} kr.')

