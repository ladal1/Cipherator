from base_cipher import Cipher


class Caesar(Cipher):
    def __init__(self, shift):
        self.shift = shift

    def encipher(self, text):
        # Takes a string, and moves its characters along the alphabet provided, in forward manner
        result = ""
        try:
            for letter in text:
                result += self.alphabet[(self.alphabet.index(letter) + self.shift) % len(self.alphabet)-1]
        except ValueError:
            print("Your text includes characters not in the entered (or default) alphabet")
            pass
        return result

    def decipher(self, text):
        result = ""
        try:
            for letter in text:
                result += self.alphabet[(self.alphabet.index(letter) - self.shift) % len(self.alphabet)-1]
        except ValueError:
            print("Your text includes characters not in the entered (or default) alphabet")
            pass
        return result

    def bruteforce(self, text):
        result = []
        try:
            for shift in range(0, len(self.alphabet)):
                step = ""
                for item in text:
                    step += self.alphabet[(self.alphabet.index(item) + shift) % len(self.alphabet)-1]
                result.append(step)
        except ValueError:
            print("Your text includes characters not in the entered (or default) alphabet")
            pass
        return result
