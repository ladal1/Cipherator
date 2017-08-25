from base_cipher import Cipher


class Keyword(Cipher):
    """
    Monoalphabethic substitution cipher, using keyword in restructuring the enciphering alphabet

    :param keyword: alphabethic key used to encipher or decipher the text
    """
    def __init__(self, keyword):
        self.key = keyword

    def encipher(self, text):
        _encrypted = self.alphabet
        result = ""
        for x in self.key:
            if x not in _encrypted:
                raise ValueError("Key cannot contain letters missing from alphabet, It is case sensitive!")
            _encrypted = _encrypted.replace(x, "")
        _encrypted = self.key + _encrypted
        for i in text:
            try:
                result += _encrypted[self.alphabet.index(i)]
            except ValueError:
                if i == " ":
                    pass
                else:
                    raise ValueError("Plaintext cannot contain letters missing from alphabet, It is case sensitive!")
        return result

    def decipher(self, text):
        _encrypted = self.alphabet
        result = ""
        for x in self.key:
            if x not in _encrypted:
                raise ValueError("Key cannot contain letters missing from alphabet, It is case sensitive!")
            _encrypted = _encrypted.replace(x, "")
        _encrypted = self.key + _encrypted
        for i in text:
            try:
                result += self.alphabet[_encrypted.index(i)]
            except ValueError:
                if i == " ":
                    pass
                else:
                    raise ValueError("Encrypted_text cannot contain letters"
                                     " missing from alphabet, It is case sensitive!")
        return result
