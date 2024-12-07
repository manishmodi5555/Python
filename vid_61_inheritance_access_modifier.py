# class a:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def show(self):
#         print(f"the name of emp {self.name} and age is {self.age}")
#
# class b(a):
#     def who(self):
#         print(f"yooo bro your in child class")
#
# obj=a("manish",20)
# obj2=b("ram",21)
# obj2.show()
# obj2.who()
from warnings import onceregistry


# #private access modifier and how to access we use __ make any variable or methods private
# class a:
#     def __init__(self):
#         self.__name='manish'# private variable
#         self.age='20'
#     def __show(self):#private method
#         print(f"hey buddy this is private methods")
#
# obj=a()
# print(obj.age)
# print(obj._a__name)#access private variable
# obj._a__show()# access private methods
#
#




# #single inheritance
# class a:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def show(self):
#         print(f" helloooo name of emp {self.name} and age is {self.age}")
#
# class b(a):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def yoo(self)            :
#         print(f"the name of emp {self.name} and age is {self.age}")
#
# obj=a("mk",40)
# obj2=b("rm",30)
# obj2.show()
# obj2.yoo()
# obj.show()
#
#


#multiple inheritance
# class a:
#     def __init__(self, age):
#         self.age = age
#
#     def yoo(self):
#         print(f" age is {self.age}")
#
# class d:
#     def __init__(self,name):
#         self.name=name
#
#     def noo(self):
#         print(f" helloooo name of emp {self.name}")
#
# class b(a,d):
#     def __init__(self, name, age): # if we change the order of the name and age (age , name )  and same methods in a and d it will print method of a first then d
#         self.name = name
#         self.age = age
#
#     def show(self):
#         print(f" helloooo name of emp {self.name} and age is {self.age}")
#
# obj2=b("rm",30)
# obj2.show()
# obj2.yoo()
# obj2.noo()

# print(b.mro())#it will show that where the method gonna find first based on order of (a,d)






#multilevel inheritance
# class a:
#     def __init__(self, name):
#         self.age = age
#
#     def yoo(self):
#         print(f" age is {self.age}")
#
# class d(a):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def noo(self):
#         print(f" helloooo name of emp {self.name}")
#
# class b(d):
#     def __init__(self, name, age): # if we change the order of the name and age (age , name )  and same methods in a and d it will print method of a first then d
#         self.name = name
#         self.age = age
#
#     def show(self):
#         print(f" helloooo name of emp {self.name} and age is {self.age}")
#
# obj2=b("rm",30)
# objd=d("kk",33)
# obj2.show()
# obj2.yoo()
# objd.yoo()
# obj2.noo()
#





# Calling
# constructor
# # of parent
# # class
#
# class a:
#     def __init__(self, num, city):
#         self.num = num
#         self.city=city
#         # self.name = name
#         # self.age = age
#
#     def yoo(self):
#         print(f" age is {self.num} city {self.city}")
#
#
# class b(a):
#     def __init__(self, name, age,num,city): # if we change the order of the name and age (age , name )  and same methods in a and d it will print method of a first then d
#         self.name = name
#         self.age = age
#
#         super().__init__(num,city)
#
#     # def show(self):
#     #     print(f" helloooo name of emp {self.name} and age is {self.age}")
#
# obj2=b("rm",30,2023,"ahemdabad")
# # obj2.show()
# obj2.yoo()
#




class duck:
    def sound(self):
        return 1

class bird:
    def sound(self):
        return 2

def makesound(rj):
    print(rj.sound())

Duck=duck()
Bird = bird()
makesound(Duck)
makesound(Bird)