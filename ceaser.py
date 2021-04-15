class Ceaser():
    def __init__(self, key, text):
        self.alphabet = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
        ]

        self.key = key
        self.text = text
        self.encrypted_text = ""
        self.decrypted_text = ""

    def encrypt(self):
        for l in self.text:
            l = l.lower()
            if l not in self.alphabet:
                self.encrypted_text += l
            else:
                self.encrypted_text += self.alphabet[(self.alphabet.index(l) + self.key) % len(self.alphabet)]
        self.decrypted_text = self.text
        return (self.encrypted_text, self.decrypted_text)

    def decrypt(self):
        for l in self.text:
            l = l.lower()
            if l not in self.alphabet:
                self.decrypted_text += l
            else:
                self.decrypted_text += self.alphabet[(self.alphabet.index(l) - self.key)]
        self.encrypted_text = self.text
        return (self.encrypted_text, self.decrypted_text)


ceaser = Ceaser(3, "OGUZBALKAYA")
print(ceaser.encrypt())

ceaser2 = Ceaser(3, "rjxcedondbd")
print(ceaser2.decrypt())
