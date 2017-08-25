from base_cipher import Cipher


class Vignere(Cipher):
    def __init__(self, passphrase):
        self.passphrase = passphrase

    def encipher(self, text):
        passletter = 0
        result = ""
        for x in text:
            result += self.alphabet[(self.alphabet.index(x) + self.alphabet.index(
                self.passphrase[passletter % len(self.passphrase)])) % len(self.alphabet)]
            passletter += 1
        return result

    def decipher(self, text):
        passletter = 0
        result = ""
        for x in text:
            result += self.alphabet[(self.alphabet.index(x)-self.alphabet.index(
                self.passphrase[passletter % len(self.passphrase)])) % len(self.alphabet)]
            passletter += 1
        return result
