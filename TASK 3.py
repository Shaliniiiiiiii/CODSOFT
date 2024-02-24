

### PASSWORD GENERATOR ###                      
###  TASK 3  ####


import random


lower = "abcdefghijklmnopqrstuvwxyz"

upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

numbers="123456789"

symbols="[]{}()*;/-_#@+"


print("WELCOME TO PASSWORD GENERATOR.....!!!!!")


all=lower+upper+numbers+symbols

length = int(input("Enter the length:"))

lower = int(input("Enter  lower needs:"))

upper = int(input("Enter upper needs:"))

numbers=int(input("Enter number needs:"))

symbols = int(input("Enter the symbol needs:"))


password = "" . join(random.sample(all,length))

print ("THE PASSWORD IS :",password)
