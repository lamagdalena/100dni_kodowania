def encrypt_decrypt_algorithm():
    default = '1234567890qwertyuiopasdfghjklzxcvbnm'
    encrypted = 'mnbvcxzlkjhgfdsapoiuytrewq0987654321'
    encrypt = str.maketrans(default, encrypted)
    decrypt = str.maketrans(encrypted, default)
    encrypt_or_decrypt = input('Do you want to encrypt (E) or decrypt (D)?')
    if encrypt_or_decrypt == 'E' or encrypt_or_decrypt == 'e' :
        to_encrypt = input('Introduce text you want to encrypt:')
        return (to_encrypt.lower()).translate(encrypt)
    elif encrypt_or_decrypt == 'D' or encrypt_or_decrypt == 'd' :
        to_decrypt = input('Introduce text you want to decrypt:')
        return (to_decrypt.lower()).translate(decrypt)
    else:
        return 'Wrong letter!'
