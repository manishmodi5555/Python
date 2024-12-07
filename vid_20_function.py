# def add(a,b):
#     c=a+b
#     print("this add")
#     return c
#
# a=10
# b=5
# d=add(a,b)
# print(d)
#
#
#
# def sub(a,b):
#     pass                 #it will pass the fun not if you want to writen fun body later
#
#
#
#
# def strinn(a,b):
#     print(a,b)
#
# strinn("manish","modi")


## default arguments
# def avg(c, a=10, b=10 ):
#     print("avg is",(a+b)/2)
#     print('c is',c)
#
# avg(5,6)


##keyword arguments
# def avg(a,b,c=10):
#     print("add ",a+b+c)
#
# avg(b=2,a=3,c=3) #order doesnt matter


##arbitrary arguments
# def avg(**name):
#     print("hello",name["fname"], name["lname"],name["mname"])
#
# avg(fname="manish" ,lname= "mukesh", mname="anil")
#
#
# def avg(*name):
#     print("hello",name[0], name[1],name[2])
#
# avg("manish" , "mukesh","anil")




## function recursion
#find factorial
# 5=5*4*3*2*1
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * fact(n-1) # this is fun call fun call in the same  fun called recursion

print(fact(5))


#fibonacci sereis
def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

for i in range(1,6):# print(fibo(6))   we write 6 but it will print for 5 6 not count you can use this insted print(fibo(6))
    print(fibo(i))

