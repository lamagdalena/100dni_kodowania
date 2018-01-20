from datetime import datetime as czas

teraz = czas.now()

def age_in_seconds():
    data_urodzenia = input('Podaj swoją datę urodzenia (w formacie RRRR-MM-DD):')
    wiek_w_sekundach = (teraz - czas.strptime(data_urodzenia, '%Y-%m-%d')).total_seconds()
    print(wiek_w_sekundach)
