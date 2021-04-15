class PlayfairCipher():
    def createList(self, key):
        matrix = list()
        key = key.upper().replace(" ", "")
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        for l in key:
            if l not in matrix and l in alphabet:
                matrix.append(l)
        for l in alphabet:
            if l not in matrix:
                matrix.append(l)
        return matrix

    def reformatText(self, text):
        text = text.upper().replace(" ", "")
        new_text = ""
        for i in range(len(text)):
            if (i > 0 and text[i] == text[i - 1]):
                new_text += 'X'
            new_text += text[i]
        if len(new_text) % 2 != 0:
            new_text += 'X'
        return new_text

    def encrypt(self, key, text):
        encryped_text = ""
        matrix = self.createList(key)
        text = self.reformatText(text)
        textList = [text[i:i + 2] for i in range(0, len(text), 2)]
        for i in textList:
            row1, column1 = matrix.index(i[0]) // 5, matrix.index(i[0]) % 5
            row2, column2 = matrix.index(i[1]) // 5, matrix.index(i[1]) % 5
            if row1 == row2:
                encryped_text += matrix[row1 * 5 + (column1 + 1) % 5]
                encryped_text += matrix[row2 * 5 + (column2 + 1) % 5]
            elif column1 == column2:
                encryped_text += matrix[((row1 + 1) % 5) * 5 + column1]
                encryped_text += matrix[((row2 + 1) % 5) * 5 + column2]
            else:  # rectangle
                encryped_text += matrix[row1 * 5 + column2]
                encryped_text += matrix[row2 * 5 + column1]
        return text, key, encryped_text

    def decryption(self, key, text):
        matrix = self.createList(key)
        decrypted_text = ""
        textList = [text[i:i + 2] for i in range(0, len(text), 2)]
        for i in textList:
            row1, column1 = matrix.index(i[0]) // 5, matrix.index(i[0]) % 5
            row2, column2 = matrix.index(i[1]) // 5, matrix.index(i[1]) % 5
            if row1 == row2:
                decrypted_text += matrix[row1 * 5 + (column1 - 1) % 5]
                decrypted_text += matrix[row2 * 5 + (column2 - 1) % 5]
            elif column1 == column2:
                decrypted_text += matrix[((row1 - 1) % 5) * 5 + column1]
                decrypted_text += matrix[((row2 - 1) % 5) * 5 + column2]
            else:  # rectangle
                decrypted_text += matrix[row1 * 5 + column2]
                decrypted_text += matrix[row2 * 5 + column1]
        return text, key, decrypted_text


deneme = PlayfairCipher()
print(deneme.encrypt("PLAYFAIREXAMPLE", "HIDETHEGOLDINTHETREESTUMP"))
print(deneme.decryption("PLAYFAIREXAMPLE", "BMODZBXDNABEKUDMUIXMMOUVIF"))
