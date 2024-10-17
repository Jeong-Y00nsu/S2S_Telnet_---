import fileIO
from cryptography.fernet import Fernet

class CryptData:
    key : str
    cipher_suit : Fernet

    def __init__(self):
        f = fileIO.FileIO()
        self.key = f.readCryptKey()
        self.cipher_suit = Fernet(self.key)

    def encryptData(self, text):
        return self.cipher_suit.encrypt(text)
    
    def decryptData(self, encryptedText):
        return self.cipher_suit.decrypt(encryptedText)
    
    def generateKey():
        tmpKey = Fernet.generate_key()
        f = fileIO.FileIO()
        f.writeCryptKey(tmpKey)
