import random
lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols=",<.>/?';:]}[{+_-!@#$%^&*()"
numbers="0123456789"
all_char=lower+upper+symbols+numbers
leng=int(input("enter length:"))
password=' '.join(random.sample(all_char,leng))
print("Generate password:",password)
