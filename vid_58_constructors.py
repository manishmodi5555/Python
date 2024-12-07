# class per:
#     def __init__(self):
#         self.name="manish"
#         self.age=20
#         # pro="hod"
#
#     def info(self):
#         print(f" {self.name} age is {self.age} ")
#
# a=per()
# a.info()

#perameterrized
class a:
    def __init__(self,c,v):
        self.name=c
        self.age=v

    def info(self):
        print(f"{self.name} age is {self.age}")

obj1=a("manish",22)
obj2=a("mukesh",21)

obj1.info()
obj2.info()