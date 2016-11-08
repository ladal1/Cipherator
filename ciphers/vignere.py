def encipher(text, passphrase, alphabet="abcdefghijklmnopqrstuvwxyz"):
    passletter = 0
    result = ""
    for x in text:
        result += alphabet[(alphabet.index(x)+alphabet.index(passphrase[passletter%len(passphrase)]))%len(alphabet)]
        passletter += 1
    return result


def decipher(text, passphrase, alphabet="abcdefghijklmnopqrstuvwxyz"):
    passletter = 0
    result = ""
    for x in text:
        result += alphabet[(alphabet.index(x)-alphabet.index(passphrase[passletter%len(passphrase)]))%len(alphabet)]
        passletter += 1
    return result
