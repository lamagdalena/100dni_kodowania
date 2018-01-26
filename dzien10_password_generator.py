import random

def password_generator():
    litery = list('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')
    cyfry = list('1234567890')
    znaki = list('!@#$%^&*()')
    wszystkie = litery + cyfry + znaki
    haslo = random.choices(wszystkie, k = random.randint(6, 25))
    return ''.join(haslo)
