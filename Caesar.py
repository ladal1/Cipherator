def encipher(text, shift ,alphabet = "abcdefghijklmnopqrstuvwxyz"):
    '''
    Takes a string, and moves its characters along the alphabet provided, in rightway manner
    '''
    result = ""
    try:
        for item in text:
            result += alphabet[alphabet.index(item) + shift]
    except ValueError:
        print("Your text includes characters not in the entered (or default) alphabet")
        pass
    return result


def decipher(text, shift, alphabet = "abcdefghijklmnopqrstuvwxyz"):
    '''
    Takes a string, and moves its characters along the alphabet provided
    '''
    result = ""
    try:
        for item in text:
            result += alphabet[alphabet.index(item) + shift]
    except ValueError:
        print("Your text includes characters not in the entered (or default) alphabet")
        pass
    return result
