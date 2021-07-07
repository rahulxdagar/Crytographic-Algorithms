""""
@author: Rahul 18BCE0018
"""
#18BCE0018
import random
import sympy
from math import pow

#Large Prime
P = int(input("Enter a Large Prime, P: "))
#Private Key
D=int(input("Enter the Private Key , D : "));

E1 = int(input("Enter E1: "))

E2=int(pow(E1,D)%P)

print("\nYou Entered :")
print("Prime P: ",P)
print("D: ",D)
print("E1: ",E1)
print("E2: ",E2)

#Final Keys Generated
print("Public Key : (",E1,",",E2,",",P,")")
print("Private Key: ",D)

#Encryption
print("\nEncryption");
R=random.randint(4,5);  #Random number R , generated
PT=int(input("Enter Plain Text, PT:"))  #Input Plain Text
C1=int(pow(E1,R)%P)
C2=int((PT*pow(E2,R))%P)
CT=(C1,C2)              #Cipher Text (C1,C2) generated

print("Random Number, R: ",R)
print("C1: ",C1)
print("C2: ",C2)
print("CipherText=",CT)

#Decryption
print("\nDecryption");
DecryptedPT=(C2*sympy.mod_inverse(int(pow(C1,D)),P))%P
print("CipherText=",CT)
print("Plain Text Calculated=",DecryptedPT)
