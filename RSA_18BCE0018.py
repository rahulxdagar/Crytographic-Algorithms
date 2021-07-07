def gcd(e,phi):
    while phi!= 0:
        c = e % phi
        e = phi
        phi= c
    return e
#input variables
d=0
p = int(input("Enter Prime P : "))
q = int(input("Enter Prime Q : "))
message = int(input("Enter Message (Number) : "))
#calculate n
n = p*q
#phi calculation
phi = (p-1)*(q-1)

#calculate e
for e in range(2,phi):
    if gcd(e,phi)== 1:
        break
#calculate d
for i in range(1,10):
    x = 1 + i*phi
    if x % e == 0:
        d = int(x/e)
        break
#print the constants
print("-------------------")
print('\nn = '+str(n))
print('e = '+str(e))
print('Phi = '+str(phi))
print('d = '+str(d))

#printing the keys
print("-------------------")
print("Public Key= ",(e,n))
print("Private Key= ",(d,n))
print("-------------------")

#Claculating and printing the ciphertext
local_cipher =pow(message,e)
cipher_text = local_cipher % n
print('\nCIPHER TEXT = '+str(cipher_text))

#Calculate and print the decrypted plaintext
print("\n******************************")
cipher=int(input("Enter the Cipher to Decrypt: "))
decrypt_t= pow(cipher,d)
decrpyted_text = decrypt_t % n
print('\nDECRYPTED TEXT = ' +str(decrpyted_text))
print("\n******************************")