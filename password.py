import random
import bcrypt  

size = int(input("Enter the length of your Password : "))
pas ="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-*/@#$%^&()<>?|"
passw= "".join(random.sample(pas,size))
print("Password : ",passw)
password = str(passw)
password = password.encode('utf-8')
hashedPassword = bcrypt.hashpw(password, bcrypt.gensalt())

print("Encrypted : ",hashedPassword)
