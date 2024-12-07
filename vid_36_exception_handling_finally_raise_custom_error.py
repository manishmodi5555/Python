#
#
# try:
#     a = int(input("enter a number"))
#     print(f"multiplication table of {a}")
#     for i in range(11):
#         print(f"{a} X {i}= {a*i}")
#
# except Exception as e:
#     print(e) # it will print the error as output
#
#
# print("it will not print ")
#
#
#
#
#
#
#
#
# try:
#     a = int(input("enter a number"))
#     print(f"multiplication table of {a}")
#     for i in range(11):
#         print(f"{a} X {i}= {a*i}")
#
# except:
#     print(" hello here is direct values ")
#




##you can also use
## except ValueError
##except IndexError
## this are handle the program error

# try:
#     a = int(input("enter a number"))
#     print(a)
#
#     a=[1,2,3]
#     print(a[5])
#
# except ValueError:
#     print(" hey this is value error")#when you pu string instead of integer
#
# except IndexError:
#     print(" hey this is index error")
#

##finally keyword it is always execute if there is error in program or not
##it is usefull in a function normal print will not execute but finally does
#
# def fun():
#     try:
#         i=[1,2,3]
#         print(i[2])
#         return 1
#
#     except:
#         print("some error is occured")
#
#     finally:
#         print("this is always execute ")
#
#     print(" i cant execute in a function ")
#
#
# x=fun()
# print(x)





##raise custom error in python using raise keyword

# a=int(input("enter any number from 0 to 9 = "))
#
# if (a>9):
#     raise print("value should be under 9")
# else:
#     print(a)



while True:
    c=input("enter a number between 0 10 or quit")
    if c=="quit":
        print("thx")
        break
    try:
        numb=int(c)
        if numb>10:
            print(f"the answe is {numb}")
        else:
            print("the number should 0 to 10")
    except ValueError:
        print("you did not entered a valid num")
    except TypeError:
        print("you enter a valid string")

