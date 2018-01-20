def temperature_converter():
    temp_w_celsjuszach = 0
    temp_w_fahrenheitach = 0
    na_celsjusze_czy_fahrenheity = input('Jeśli chcesz zamienić temperaturę w stopniach Fahrenheita na stopnie Celsjusza to wpisz F. Jeśli chcesz zamienić temperaturę w stopniach Celsjusza na stopnie Fahrenheita to wpisz C.')
    if na_celsjusze_czy_fahrenheity == 'F':
        na_celsjusze = input('Jeśli chcesz zamienić temperaturę w stopniach Fahrenheita na stopnie Celsjusza to wpisz ją tu (SAMĄ LICZBĘ):')
        temp_w_celsjuszach = 5/9 * (int(na_celsjusze) - 32)
        if temp_w_celsjuszach < -273.15:
            return 'Ta temperatura nie istnieje - jest poniżej zera absolutnego'
        elif -273.15 > temp_w_celsjuszach > 0 :
            return 'Podana w stopniach Fahrenheita temperatura {} w przeliczeniu na stopnie Celsjusza wynosi {}. Jest to temperatura poniżej zera.'.format(na_fahrenheity, temp_w_fahrenheitach)
        elif temp_w_celsjuszach == 0:
            return 'Wynik to temperatura zamarzania wody, czyli 0 stopni Calsjusza.'
        elif temp_w_celsjuszach == 100:
            return 'Wynik to temperatura wrzenia wody, czyli 100 stopni Celsjusza.'
        else:
            return 'Podana w stopniach Fahrenheita temperatura {} w przeliczeniu na stopnie Celsjusza wynosi {}.'.format(na_celsjusze, temp_w_celsjuszach)
    elif na_celsjusze_czy_fahrenheity == 'C':
        na_fahrenheity = input('Jeśli chcesz zamienić temperaturę w stopniach Celsjusza na stopnie Fahrenheita to wpisz ją tu (SAMĄ LICZBĘ):')
        if int(na_fahrenheity) < -273.15:
            return 'Wprowadzona liczba jest niewłaściwa - poniżej zera absolutnego'
        else:
            temp_w_fahrenheitach = 32 + (9/5) * int(na_fahrenheity)
            return temp_w_fahrenheitach
    else:
        return 'Wprowadzono nieprawidłową informację.'
