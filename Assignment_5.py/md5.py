import hashlib
message = input("enter the message:")
md5_hash = hashlib.md5()
md5_hash.update(message.encode())
print(md5_hash.hexdigest())
