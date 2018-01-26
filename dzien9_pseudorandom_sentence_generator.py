import random
import json

def pseudorandom_sentence_generator():
    filename = "tekst_json.json"
    plik = open("tekst.txt")
    zawartosc = plik.read()
    with open(filename, "w") as fp:
        json.dump(zawartosc, fp)
    plik.close()
    with open(filename, "r") as fp:
        tekst_w_json = json.load(fp)
    zdania = nowy_slownik2.replace('?', '. ').replace('!', '. ').split('. ')
    random_sentence = random.choice(zdania)
    return random_sentence
