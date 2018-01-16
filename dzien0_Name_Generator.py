import random

def name_generator():
    imiona_zenskie = ['Ewa', 'Anna', 'Patrycja', 'Ewelina', 'Małgorzata', 'Dorota', 'Katarzyna']
    imiona_meskie = ['Filip', 'Alojzy', 'Marek', 'Damian', 'Jakub', 'Krzysztof', 'Piotr']
    nazwiska = ['Nowak', 'Gorzelańczyk', 'Pośpiech', 'Pilipczuk', 'Nitrowicz', 'Ryłko', 'Korek']
    
    plec = input('Wybierz płeć: m (męska) lub f (żeńska) :' )
    
    if plec == 'm':
        return 'Od dziś nazywasz się {} {}.'.format(random.choice(imiona_meskie), random.choice(nazwiska))
    elif plec == 'f':
        return 'Od dziś nazywasz się {} {}.'.format(random.choice(imiona_zenskie), random.choice(nazwiska))
    else:
        return 'Spróbuj jeszcze raz'
