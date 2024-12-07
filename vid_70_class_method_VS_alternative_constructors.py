# #class methods are used to change class variable check book, and class methods can be used as a alternativ of constructor and need to use self default argument
# # we can us cls , or anyting any name
# # @classmethod decorators use beofore starting class methods
# # lets see an example if you have a list, or tuple in a variable and if you want to pass as a argument in a constructor you can use class methods to pass
#
# class emp:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#
#     @classmethod ## it is alternativ of constructor becouse it pass a particular formate data  and also return the data instead construcor initialize var
#     def fmstr(cls,string):
#         return cls(string.split("-")[0],int(string.split("-")[1]))
#
# e1=emp("manish",200)
# print(f"{e1.name} kaaaa salary {e1.salary} hai")
#
# string="manish-1200"#if you have data like that its is hard to send string for arguments
# e2=emp.fmstr(string) # paas the whole string in claas methods by calling class methods
# print(f"{e2.name} ka salary {e2.salary} hai")
#
#


# or

class emp:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    @classmethod
    def fmstr(cls,string):
        name,salary=string.split("-")
        return cls(name,int(salary))

e2=emp.fmstr("mukesh-2000")
print(f"{e2.name} ka salary {e2.salary} hai")