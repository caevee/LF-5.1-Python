import random

laengePw = 0
pw = ""

while laengePw < 10:
    random_num = random.randint(0,127)
    if random_num > 32:
        zeichen = chr(random_num)
        pw += zeichen
        laengePw += 1

print(pw)