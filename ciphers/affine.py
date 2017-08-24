from base_cipher import Cipher


class Affine(Cipher):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def encipher(self, text):
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
