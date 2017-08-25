from math import gcd
from base_cipher import Cipher


class Affine(Cipher):
    """
    Affine cipher is a substitution cipher using two components of a key, a and b with each letter being encrypted
    through following equation::
        enciphered = (A*letter + B) % 26


    :param a: key parameter A
    :param b: key parameter B
    """
    def __init__(self, a, b):
        self.a = a
        self.b = b
        assert 0 < a and 0 <= b and a.is_integer() and b.is_integer(), \
            "Neither of the key components can be negative and a cannot be zero"

    def encipher(self, text):
        assert not bool(gcd(self.a, self.b)-1), ""
        result = ""
        try:
            for x in text:
                result += self.alphabet[(self.a * self.alphabet.index(x) + self.b) % len(self.alphabet)]
        except ValueError:
            print("Your text includes characters not in the entered (or default) alphabet")
            pass
        return result

    def decipher(self, text):
        result = ""
        try:
            for x in text:
                result += self.alphabet[(len(self.alphabet)-self.a)*(self.alphabet.index(x)-self.b) % 26]
        except ValueError:
            print("Your text includes characters not in the entered (or default) alphabet")
            pass
        return result
