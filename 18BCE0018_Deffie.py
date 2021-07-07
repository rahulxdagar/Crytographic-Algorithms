"""
Created on Fri Apr 23 20:49:24 2021

@author: rahul_18BCE0018
"""
q = int(input("Enter a Prime number : "))

# A primitve root for q, alpha is taken
alpha = int(input("Enter the Primitice root alpha : "))


print('The Value of q is :%d'%(q))
print('The Value of alpha is :%d'%(alpha))

# Alice will choose the private key a
Xa = int(input("Enter Private Key Xa: "))
print('The Private Key a for Alice is :%d'%(Xa))

# gets the generated key
Ya = int(pow(alpha,Xa,q))

# Bob will choose the private key b
Xb = int(input("Enter Private Key Xb: "))
print('The Private Key b for Bob is :%d'%(Xb))

# gets the generated key
Yb = int(pow(alpha,Xb,q))


print("\nSecret keys for Alice and Bob\n")
ka = int(pow(Yb,Xa,q))

kb = int(pow(Ya,Xb,q))

print('Secret key for the Alice is, Ka : %d'%(ka))
print('Secret Key for the Bob is, Kb : %d'%(kb))
    
if(ka==kb):
    print("\nKey Matched. Key exchange successfull.")
