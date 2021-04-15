import random

class OneTimePad():
    def strintToBinary(self,text):
        binary = ""
        for l in text:
            binary += bin(ord(l))
        return binary.replace("0b","0")

    def createRandomKey(self,lenText):
        key = ""
        for i in range(lenText):
            rand = random.randint(0,1)
            key += str(rand)
        return key

    def xor(self, a, b):
        if a == b:
            return 0
        return 1

    def encrypt(self,text):
        binaryText = self.strintToBinary(text)
        key = self.createRandomKey(len(binaryText))
        print(key)
        encrypted_text = ""
        for i in range(0,len(binaryText)):
            encrypted_text+=str(self.xor(int(binaryText[i]),int(key[i])))
        return text,encrypted_text

    def decrypt(self,text,key):
        decrypted_binary = ""
        for i in range(0,len(text)):
            decrypted_binary += str(self.xor(int(text[i]), int(key[i])))
        splited = [decrypted_binary[i:i+8] for i in range(0,len(decrypted_binary),8)]
        decrypted_string = ""
        for i in splited:
            decrypted_string+=chr(int(i, 2))
        return decrypted_binary,decrypted_string



deneme = OneTimePad()
print(deneme.encrypt("OGUZ"))
print(deneme.decrypt("00110010001110100010110111110010","01111101011111010111100010101000"))
