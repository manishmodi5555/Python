num=20
num1=30
print(num+ num1)
print(num.__add__(num1))
print(int.__add__(num,num1))

print(dir(int))


#addition without with charactor
# class vector:
#     def __init__(self,i,j):
#         self.i=i
#         self.j=j
#     def __str__(self):
#         return f"{self.i}i + {self.j}j"
#     def __add__(self, x): # (V1 in self, V2 in x)# there is no inbulilt add function in vector class so you have to define add to addition of any 2 num of char using object type of class(vector)
#         return vector(self.i+x.i  ,self.j+x.j)#v1 se i lega + v2 se i lega
#
# v1=vector(4,6)
# print(v1)
#
# v2=vector(2,3)
# print(v2)
#
# print(v1+v2)