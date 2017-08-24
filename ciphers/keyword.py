def encipher(plaintext, key, alphabet="abcdefghijklmnopqrstuvwxyz"):
    _encrypted = alphabet
    result = ""
    for x in key:
        if x not in _encrypted:
            raise ValueError("Key cannot contain letters missing from alphabet, It is case sensitive!")
        _encrypted = _encrypted.replace(x, "")
    _encrypted = key + _encrypted
    for i in plaintext:
        try:
            result += _encrypted[alphabet.index(i)]
        except ValueError:
            if i == " ":
                pass
            else:
                raise ValueError("Plaintext cannot contain letters missing from alphabet, It is case sensitive!")
    return result


def decipher(encrypted_text, key, alphabet="abcdefghijklmnopqrstuvwxyz"):
    _encrypted = alphabet
    result = ""
    for x in key:
        if x not in _encrypted:
            raise ValueError("Key cannot contain letters missing from alphabet, It is case sensitive!")
        _encrypted = _encrypted.replace(x, "")
    _encrypted = key + _encrypted
    for i in encrypted_text:
        try:
            result += alphabet[_encrypted.index(i)]
        except ValueError:
            if i == " ":
                pass
            else:
                raise ValueError("Encrypted_text cannot contain letters missing from alphabet, It is case sensitive!")
    return result
