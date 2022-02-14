def my_input() -> int:
    while True:
        try:
            result = int(input('Type a number or ^C to cancel :'))
        except ValueError:
            print("Please enter a valid number")
        except KeyboardInterrupt:
            print("\nInput canceled")
            return None
        else:
            return result
        
i = my_input()
if i is not None:
    print("User input %d" % i)