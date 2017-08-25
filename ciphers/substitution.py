from base_cipher import Cipher


class Substitution(Cipher):
    def __init__(self, alphabet2):
        self.alphabet2 = alphabet2
        assert type(alphabet2) is str, "alphabet2 must be a string respresenting alphabet to which you are converting"

    def encipher(self, text):
        result = ""
        try:
            for x in text:
                result += self.alphabet2[self.alphabet.index(x)]
        except ValueError:
            raise ValueError("Text can't contain letters missing from alphabet")
        return result

    def decipher(self, text):
        result = ""
        try:
            for x in text:
                result += self.alphabet[self.alphabet2.index(x)]
        except ValueError:
            raise ValueError("Text can't contain letters missing from alphabet")
        return result
