qus=[
    ["captial of india ?","delhi","rajsthan","bihar","mumbai","none",4],
    ["captial of india ?", "delhi", "rajsthan","bihar", "mumbai","none",4],
    ["captial of india ?", "delhi", "rajsthan","bihar", "mumbai","none",4],
    ["captial of india ", "delhi", "rajsthan","bihar", "mumbai","none",4],
    ["captial of india ", "delhi", "rajsthan","bihar", "mumbai","none",4],
    ["captial of india ", "delhi", "rajsthan","bihar", "mumbai","none",4],
    ["captial of india ", "delhi", "rajsthan","bihar", "mumbai","none",4],
    ["captial of india ", "delhi", "rajsthan","bihar", "mumbai","none",4],
    ["captial of india ", "delhi", "rajsthan","bihar", "mumbai", "none", 4],
    ["captial of india ", "delhi", "rajsthan","bihar", "mumbai", "none", 4],
    ["captial of india ", "delhi", "rajsthan","bihar", "mumbai", "none", 4],
    ["captial of india ", "delhi", "rajsthan","bihar", "mumbai", "none", 4],
    ["captial of india ", "delhi", "rajsthan","bihar", "mumbai", "none", 4],
    ["captial of india ", "delhi", "rajsthan","bihar", "mumbai", "none", 4],
    ["captial of india ", "delhi", "rajsthan","bihar", "mumbai", "none", 4],
    ["captial of india ", "delhi", "rajsthan","bihar", "mumbai", "none", 4],
    ["captial of india ", "delhi", "rajsthan","bihar", "mumbai", "none", 4],
    ["captial of india ", "delhi", "rajsthan","bihar", "mumbai", "none", 4],
    ["captial of india ", "delhi", "rajsthan","bihar", "mumbai", "none", 4],
    ["captial of india ", "delhi", "rajsthan","bihar", "mumbai", "none", 4],
    ["captial of india ", "delhi", "rajsthan","bihar", "mumbai", "none", 4],
    ["captial of india ", "delhi", "rajsthan","bihar", "mumbai", "none", 4],
    ["captial of india ", "delhi", "rajsthan","bihar", "mumbai", "none", 4],
    ["captial of india ", "delhi", "rajsthan","bihar", "mumbai", "none", 4],
    ]

level=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000]
money=0

for i in range(0, len(qus)):
    qus2=qus[i]
    print(f"\n\n question for Rs:{level[i]}")
    print(f"a.{qus2[1]}               b.{qus2[2]}")
    print(f"c.{qus2[3]}               d.{qus2[4]}")

    rep=int(input("enter your answer 1 to 4 or press 0 to quit the game "))

    if(rep == 0):
        money=level[i-1]
        break
    if(rep==qus2[-1]):
        print("currect answer")
        print(f"you won RS:{level[i]}")
        if(i==4):
            money=10000
        elif(i==9):
            money=320000
        elif(i == 14):
            money = 10000000
    else:
        print("wrong answer")
        break

print(f"your tatal ammount you take home{money}")
#
# def dev():
#     print(f"your tatal ammount you take home{money}")