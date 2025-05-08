import hashlib
message = input("enter the message:")
sha1_hash = hashlib.sha1()
sha1_hash.update(message.encode())
result = sha1_hash.hexdigest()
print(result)
