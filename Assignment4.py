from Crypto.cipher import AES
key = input("enter the key:")
key_size = len(16)
cipher = AES.new(key, AES.MODE_EAX)
data = input("enter the message:")
endata=data.encode()
nonce=cipher.nonce
ciphertext = cipher.encrypt(data)
print("ciphertext is",ciphertext)
cipher = AES.new(key, AES.MODE_EAX,nonce = nonce)
plaintext = cipher.decrypt(ciphertext)
print("plain text",plaintext.decode())
###########################################################3

from Crypto.Cipher import AES
key = b'C&F)H@McQf9TjWnZr'
cipher = AES.new(key, AES.MODE_EAX)
data = "Welcome to copyassignment.com!".encode()
nonce = cipher.nonce
ciphertext = cipher.encrypt(data)
print("Cipher text:", ciphertext)
cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
plaintext = cipher.decrypt(ciphertext)
print("Plain text:", plaintext)
################################################################3
from Crypto.Cipher import DES

key = input("enter the key:").encode()  # Encode key to bytes
# DES key must be exactly 8 bytes
if len(key) != 8:
    raise ValueError("Key must be exactly 8 bytes long.")

cipher = DES.new(key, DES.MODE_EAX)

data = input("enter the message:")
endata = data.encode()  # Convert message to bytes

nonce = cipher.nonce
ciphertext = cipher.encrypt(endata)

print("ciphertext is", ciphertext)

cipher = DES.new(key, DES.MODE_EAX, nonce=nonce)
plaintext = cipher.decrypt(ciphertext)

print("plain text", plaintext.decode())
#########################################################33
from Crypto.Cipher import AES
key = input("enter the key:").encode() 
cipher = AES.new(key, AES.MODE_EAX)

data = input("enter the message:")
endata = data.encode()  

nonce = cipher.nonce
ciphertext = cipher.encrypt(endata)  
print("ciphertext is", ciphertext)

cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
plaintext = cipher.decrypt(ciphertext)

print("plain text", plaintext.decode())
