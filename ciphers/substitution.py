def cipher(text, to_alphabet, from_alphabet="abcdefghijklmnopqrstuvwxyz"):
    result = ""
    for x in text:
        result += to_alphabet[from_alphabet.index(x)]
    return result


def bruteforce(text, to_alphabet):
    pass