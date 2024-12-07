# tup=(1,2,3,4,5)
# tup2=('mansih''mukesh''suresh''rakesh')
# print(type(tup))
# print(len(tup))
# # tup[0]=9 # it will thorw error tuple is immutable
# print(tup)
#
# # all things are similer to list
#
# print(tup[1:3])
# print(tup[1:])
# print(tup[:4])
# print(tup[-1])#len - 1 = index value
#
# if 2 in tup:
#     print("yes bro")




## methods of tuple

tup= (1,2,3,4,5,5,6,8,3)
temp = list(tup)# if you want to make changes in tuple you have to change tup into list and you can apply list methods
temp.append(10)
temp.pop(3)
temp[5]="manish"
tup=tuple(temp)
print(tup)



res=tup.count(3)
print(res)



res=tup.index("manish")
print(res)
res2=tup.index(5,3,8)
print(res2)
