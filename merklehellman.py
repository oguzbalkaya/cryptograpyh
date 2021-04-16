import random
from numpy import gcd

class MerkleHellman():
    def isSuperIncreasing(self, list):
        for i in range(len(list) - 1, -1, -1):
            if list[i] < sum(list[0:i]):
                return 0
        return 1

    def createKey(self, superincreasing):
        if 0 in superincreasing:
            raise ValueError("The list can not contain 0.")
        elif not self.isSuperIncreasing(superincreasing):
            raise ValueError("The list is not superincreasing.")
        k = random.randint(1, 2) + 1
        q = random.randint(sum(superincreasing), sum(superincreasing) * k)
        r = random.randint(2, 4 * q)
        while gcd(q, r) != 1:
            r = random.randint(1, 4 * q)
        beta = [(r * superincreasing[i]) % q for i in range(0, len(superincreasing))]
        return beta,(superincreasing,q,r)

    def encrypt(self,superincreasing,text):
        text=text.upper().replace(" ","")
        keys = self.createKey(superincreasing)
        beta = keys[0]
        encryepted = list()
        for i in text:
            alfa = bin(ord(i)).replace("0b","0")
            c = 0
            for j in range(0,8):
                c += int(beta[j])*int(alfa[j])
            encryepted.append(c)
        #print(keys)
        return text,beta,encryepted

    def subSetSum(self,mainlist,value):
        sum,indexes = 0,list()
        for i in range(len(mainlist)-1,-1,-1):
            if sum == value:
                return indexes
            if mainlist[i] <= value-sum:
                sum += mainlist[i]
                indexes.append(i)
        return indexes


    def calculateS(self,r,q):
        for s in range(1,q):
            if r*s%q == 1:
                return s
        else:
            raise ValueError("err")

    def decrypt(self,w,q,r,text):
        decrypted = ""
        s = self.calculateS(r,q)
        for c in text:
            c_ussu=(c*s)%q
            indexes = self.subSetSum(w,c_ussu)
            binary = ""
            for i in range(8):
                if i in indexes:
                    binary+=str(1)
                else:
                    binary+=str(0)
            decrypted+=(chr(int(binary, 2)))
        return text,decrypted

try:
    mh = MerkleHellman()
    print(mh.encrypt([2, 7, 11, 21, 42, 89, 180, 354],"OGUZBALKAYA"))
    print(mh.decrypt([2, 7, 11, 21, 42, 89, 180, 354],1648,5757,[5792, 4606, 3883, 3842, 2063, 1797, 3426, 4299, 1797, 3576, 1797]))
except ValueError as err:
    print(err)
