import random
import string

def encoding(sto):
    messange=sto
    if len(messange)>3:
        messange=messange[1:]+messange[0]
        char=''.join(random.choices(string.ascii_letters,k=3))
        char2=''.join(random.choices(string.ascii_letters,k=3))
        messange=char+messange+char2

    else:
        messange=messange[::-1]

    return messange




def decoding(secret_code):
    messange=secret_code
    if len(messange)>6:
        messange=messange[3:-3]
        messange=messange[-1]+messange[:-1]
    else:
        messange=messange[::-1]

    return messange



sto = input("enter your mmassage")
print(f"your message is {sto}  ")

c=int(input("if you want to encode your messange please press 1"))

if(c==1):
    secret_code = encoding(sto)
else:
    print("invelid input")

print(f"your encoded messange is here {secret_code}")



d=int(input("if you want decode your message please press 2\n"))
if(d==2):
    dcoded = decoding(secret_code)
else:
    print("invelid input")

print(f"your encoded messange is here {dcoded}")