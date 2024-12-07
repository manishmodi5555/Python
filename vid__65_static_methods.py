# #instance methods
# class a:
#     @staticmethod
#     def add(a,b):
#         return a+b
#
# print(a.add(1,2))
# obj=a()
# # print(result)
# print(obj.add(4,5))



#instance variable and class variable
#defined in class inside a methods called instance var and define inside a  class but outside of a methods called class var
class b:
    class_var=0#class variable can access by class name
    def __init__(self):
        self.a=10 # instance variable
        b.class_var += 1 # class variale called using class name
    def add(self):
        print(f"{self.a*2}")

obj=b()
print(obj.a)
obj.a=100
print(obj.a)

print(obj.class_var)

obj2=b()
obj2.add()
print(obj2.a)

print(obj2.class_var,"this is class variable increasing their values when  its create new obj")
print(obj.class_var,'still 2 becouse its changed')
print(b.class_var)#2
b.class_var=5 # changing class var
print(b.class_var)#5
print(obj.class_var)#5