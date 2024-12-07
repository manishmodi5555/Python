# def cube(x):
#     return x*x*x
# print(cube(2))
# l=[1,2,3,4,5]
# #use of MAP
# # if want to find cube of every elements in a list
# new=list(map(cube,l))
# print(new)
# #or you can use this new=map(lambda x:x*x*x,l)
# #print(list(new))


# ##use of filter
# #print even number elements are added into newl who satisfied given condition it take input in sequence of elements and give output as sequence of elements
# num=[1,2,3,4,5,6,7]
# newl=filter(lambda x:x%2==0,num)
# print(list(newl))



## use of reduce higher order function 3rd
##first we have to import reduce fun before use

# from functools import reduce
# numm=[1,2,3,4,5] 
# sum=reduce(lambda x,y:x+y,numm)   #1+2=3 , 3+3=6,6+4+10,10+5=15
# print(sum)    # no need to convert into list