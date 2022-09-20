import random

password = int(input("Enter the length of your Password : "))
pas ="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-*/@#$%^&()<>?|"
passw= "".join(random.sample(pas,password ))
print(passw)