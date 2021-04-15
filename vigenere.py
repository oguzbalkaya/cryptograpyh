import pandas as pd, string


class Vigenere():
    def __init__(self):
        pass

    def createTable(self):
        data = list()
        for i in range(26):
            left = string.ascii_uppercase[i:]
            right = string.ascii_uppercase[:i]
            data.append(list(left + right))
        vigenere_table = pd.DataFrame(data, columns=list(string.ascii_uppercase), index=list(string.ascii_uppercase))
        return vigenere_table

    def keyControl(self, text, key):
        key=key.replace(" ","")
        if len(key) > len(text):
            raise ValueError
        elif len(key) < len(text):
            for i in range(0, len(text) - len(key)):
                key += key[i]
        return key

    def encrypt(self, text, key):
        text = text.upper().replace(" ","")
        vigenere_table = self.createTable()
        key = self.keyControl(text, key)
        encrypted_text = ""
        for i in range(0, len(text)):
            encrypted_text += vigenere_table[text[i]][key[i]]
        return text, key, encrypted_text

    def decrypt(self, text, key):
        text = text.upper().replace(" ","")
        key = self.keyControl(text, key)
        vigenere_table = self.createTable()
        decrypted_text = ""
        for i in range(0, len(text)):
            decrypted_text += vigenere_table.index[vigenere_table[key[i]] == text[i]].item()
        return text, key, decrypted_text


try:
    vig = Vigenere()
    print(vig.encrypt("ATTACKATDAWN", "LEMON"))
    print(vig.decrypt("LXFOPVEFRNHR", "LEMON"))
except ValueError:
    print("error")
