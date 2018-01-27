def collatz_conjecture():
    liczba = input('Introduce a number you want to start with : ')
    liczba = int(liczba)
    steps = 0
    if liczba > 0:
        while liczba != 1:
            if liczba % 2 == 0:
                liczba = liczba/2
                print(int(liczba))
            else:
                liczba = 3 * liczba + 1
                print(int(liczba))
            steps +=1
            
    return 'Reached 1 in ' + str(steps) + ' steps'
