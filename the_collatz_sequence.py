# A program that lets the user type in an integer 
# and that keeps calling collatz() on that number until the function returns the value 1

def collatz():
    while True:
        number = input('Hi, please type in an integer, or "exit" to stop the programme:\n')

        if number.lower() == "exit":
            print('Bye')
            break
        
        try:
            number = int(number)

            if number <= 0:
                print('Please input a positive integer')

            while number != 1 and number > 0:
                if number % 2 == 0:
                    number = number//2
                    print(number)
                else:
                    number = 3 * number + 1
                    print(number)
        
        except(ValueError):
            print('Please input a valid integer.')

collatz()