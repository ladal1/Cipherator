class Cipher:
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    def encipher(self, text):
        pass

    def decipher(self, text):
        pass

    def l2num(self, ch):
        return self.alphabet.index(ch)

    def num2l(self, num):
        return self.alphabet[num]
