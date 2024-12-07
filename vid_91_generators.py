 # check book it generate values on fly this is not store the values it is use next() fun to access values yield define generator fun and it return object
 # this is also hold its last stage doesnot print single value multiple times
# def my_gen():
#     yield "this is 1st value"
#     yield "this is 2nd value"
#     yield "this is 3rd value"
#
# g=my_gen()
# print(type(g))
# print(next(g))
# print("-----------------")
# for ele in g:
#     print(ele)




#simple program
import time
def countdown(num):
    print("countdown start...")
    while num>0:
        yield num
        num=num-1
g=countdown(5)
print(next(g))
print("one time only ")

for ele in g:
    print(ele)