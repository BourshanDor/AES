from AES import AES 
from PKCS import padding 
from  base64 import b64decode, b64encode


class CBC(AES) : 
  
  def __init__(self, key,  iv = bytearray(16)) :
    super().__init__(key)
    self.iv = iv 

  def cbcEncrypt(self, data : bytes) :

    cipherPrev = self.iv
    state = bytearray()
    for i in range(0, len(data), 16) : 
      if i + 16 > len(data) : 
        message = padding(data[i : ])
      else : 
        message = data[i : i + 16]
      cipherPrev = self.encrypt(bytes([_b1 ^ _b2 for _b1, _b2 in zip(cipherPrev, message)]))
      state += cipherPrev 
    return bytes(state)
    
  def cbcDecrypt(self, data : bytes) :

    cipherPrev = self.iv
    state = bytearray()
    for i in range(0, len(data), 16) : 
      if i + 16 > len(data) : 
        message = padding(data[i : ])
      else : 
        message = data[i : i + 16]
      
      plainText = self.decrypt(message)
      plainText = bytes([_b1 ^ _b2 for _b1, _b2 in zip(cipherPrev, plainText)])
      state += plainText 
      cipherPrev = message 
    return bytes(state)


if __name__  == '__main__' : 
  
  encodedCipherText = open(r"/home/dorbourshan/projects/Self_Study/crypto/set2/static/challenge10.txt", "r").read()

  cipherText = b64decode(encodedCipherText)
  key = 'YELLOW SUBMARINE'

  cipher = CBC(key) 

  text = cipher.cbcDecrypt(cipherText)
  print(text.decode('utf-8'))
  
