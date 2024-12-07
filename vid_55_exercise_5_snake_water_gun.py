import random
comp=random.randint(0,2)
user=int(input("enter 0 ,1 or 2 , 0 for rock,\n 1 for peper \n 2 for scissors\n"))

def check(user, comp):

    if comp==user:
        return 0
    if(user==0 and comp==1):
        return -1
    if(user==1 and comp==2):
        return -1
    if(user==2 and comp==0):
        return -1
    return 1

score=check(user,comp)
print(f"your computer choose {comp}")
if score ==0:
    print("this is drow")
elif score==1:
    print("you won")
else:
    print("you lost")