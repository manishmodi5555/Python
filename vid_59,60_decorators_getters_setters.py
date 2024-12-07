# def greet(fx):
#     def mfx():
#         print("hey good morning")
#         fx()
#         print('thanku for using this fun')
#     return mfx
#
# @greet
# def hello():
#     print("hello world")
#
# hello()
# # we can called function using this removoe hello() and @greet then use  " greet(hello)() " () use for arguments
#



# #argunments
# def greet(kj):
#     def mhj(*args):
#         print("hey good morning")
#         kj(*args)
#         print('thanku for using this fun')
#     return mhj
# @greet
# def add(a,b):
#     print(a+b)
# add(1,2)



#getters is methods is behave like a property we can also print it but this is a methods(fun) we can set any values useing setter we can set values for a method
#
# class my:
#     def __init__(self,value):
#         self._value=value
#
#     def show(self):
#         print(f"value is {self._value}")
#
#     @property
#     def ten_values(self):
#         return 10* self._value
#
# obj=my(10)
# print(obj.ten_values)
# obj.show()
#


#setters
class my:
    def __init__(self,value):
        self._value=value

    def show(self):
        print(f"value is {self._value}")

    @property
    def any_name(self):
        return 10* self._value

    @any_name.setter
    def any_name(self,newval):
        self._value=newval/10


obj=my(10)
obj.any_name=200
print(obj.any_name)
obj.show()