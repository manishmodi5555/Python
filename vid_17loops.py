# a="mansish"
# for char in a:
#     print(char)

## printing elemnets of list
# b=["mans","mukesh","jay"]
# for char in b:
#     print(char)
#     for i in char:
#         print(i)


##printing numbers using range
# for i in range(10):
#     print(i+1)


## printing numbers between specfic range also use third parameter of range which make gap between numbers understand the example
# for i in range(2,10,3):      ##make 3 numbers gap range(start, stop, step)
#     print(i)



##while loop
# i=5
# while(i>0):
#     print(i)
#     i=i-1
# else:
#     print("im out")
#
# #break and continue statements
# while True:
#     print("hey")
#     break
#



## break skip the loop
# for i in range(15):
#     if (i == 10):
#         break
#     print("5 X",i+1,"=",5*(i+1))
#
# print("im out")


## continue statement skip the iteration
# for i in range(15):
#     if (i == 10):
#         continue# it will not print table for 10
#     print("5 X",i,"=",5*i)
# print("im out")



# print prime number
for num in range(1, 20):
    if num > 1:  # Prime numbers are greater than 1
        for i in range(2, num):
            if num % i == 0:
                break # it will break the loop not print else goes to outer loop
        else:
            print(num)


