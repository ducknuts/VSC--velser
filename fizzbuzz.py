for x in range (1, 30):
    if x % 3 == 0:
        print(f"{x}: Fizz")
    if x % 5 == 0:
        print(f"{x}: Buzz")
    if x % 3 == 0 and x % 5 == 0:
        print(f"{x}: FizzBuzz")
    else:
        print(x)

