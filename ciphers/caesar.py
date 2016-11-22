def cipher(text, shift, alphabet="abcdefghijklmnopqrstuvwxyz"):
    # Takes a string, and moves its characters along the alphabet provided, in forward manner
    result = ""
    try:
        for letter in text:
            result += alphabet[(alphabet.index(letter) + shift)%len(alphabet)]
    except ValueError:
        print("Your text includes characters not in the entered (or default) alphabet")
        pass
    return result


def bruteforce(text, alphabet="abcdefghijklmnopqrstuvwxyz"):
    result = []
    try:
        for shift in range(0, len(alphabet)):
            step = ""
            for item in text:
                step += alphabet[(alphabet.index(item) + shift)%len(alphabet)]
            result.append(step)
    except ValueError:
        print("Your text includes characters not in the entered (or default) alphabet")
        pass
    return result
