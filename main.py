import random

codes = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

lengthinserting = int(input("insert length of the password"))

password = ""

for i in range(lengthinserting):

    password += random.choice(codes)

print(password)