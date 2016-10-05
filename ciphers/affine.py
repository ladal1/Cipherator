from itertools import product

def encipher(a, b, text, alphabet="abcdefghijklmnopqrstuvwxyz"):
    result = ""
    try:
        for x in text:
            result += alphabet[(a * alphabet.index(x) + b)%len(alphabet)]
    except ValueError:
        print("Your text includes characters not in the entered (or default) alphabet")
        pass
    return result

