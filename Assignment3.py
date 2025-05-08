p = int(input("enter the prime number:"))
p_r = int(input("enter the primitive root:"))
x_a = int(input("enter the private key of alice:"))
x_b= int(input("enter the private key of bob:"))
y_a = pow(p_r,x_a,p)
print("The public key of alice is:",y_a)
y_b = pow(p_r,x_b,p)
print("The public key of bob is:",y_b)
sec_a = pow(y_b,x_a,p)
print("The secret key of alice is:",sec_a)
sec_b = pow(y_a,x_b,p)
print("The secret key of bob is:",sec_b)
if sec_a == sec_b:
    print("The secret keys are matched!! The key exchange is successfully done!!!")
else:
    print("Not done!!!")


























