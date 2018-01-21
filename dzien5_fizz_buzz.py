def fizz_buzz():
    max_number = input('What is your end number?')
    for number in range(1, (int(max_number) + 1)):
        if number % 3 == 0 and number % 5 == 0:
            print('FIZZBUZZ')
        elif number % 3 == 0:
            print('FIZZ')
        elif number % 5 == 0:
            print('BUZZ')
        else:
            print(number)
