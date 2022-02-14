from hashlib import new


new_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(new_list[:11:-1])
# print(new_list[11:7:-1])
# print(new_list[7:3:-1])
# print(new_list[3::-1])

#new_list = 10101001
byte = 69
for i in range(8):
    print ([byte >> i & 1 for i in range(8)])