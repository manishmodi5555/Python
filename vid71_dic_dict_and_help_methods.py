#use of dir
# x=[1,2,3]#list
# a=(1,2,3)#tuple
# print(dir(x))# dir is a function return all attribute and methods of a object[tuple].
# print(x.__add__) # define use of add in dir x
# print(dir(a))



# use of __dict__  attribute return a dictionary representation of an object attributes it is a usefull tool for introsprection
# class a:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         self.city="ahemdabad"
#
# obj=a("manish",20)
# print(obj.__dict__)# it is return value in key pair which is in self only




# help methods it is fun used to get help documentation for an object include desription of its and methods
# print(help(str))
print(help(int))