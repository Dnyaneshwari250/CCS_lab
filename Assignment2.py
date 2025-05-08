from math import gcd
p = int(input("enter the first prime number:"))
q = int(input("enter the second prime number:"))
n = p * q
z= ((p-1)*(q-1))
e =int(input("enter the value of e 1 < e < {z} and gcd(e,{z} = 1):"))
def mod_inverse (e, z):
    for i in range(1, z):
        if (e * i) % z ==1:
            return i
    return none 
i = mod_inverse (e, z)
m = int(input("enter the message (0 < m < {n}):"))
c = pow (m, e ,n)
decrypted_m = pow(c, i, n)
print(f"\nPublic Key: (e={e}, n={n})")
print(f"Private Key: (i={i}, n={n})")
print(f"Message: {m}")
print(f"Encrypted Message: {c}")
print(f"Decrypted Message: {decrypted_m}")