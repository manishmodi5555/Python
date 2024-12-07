marks=[22,23,12,34,21]
for index, i in enumerate(marks):
    print(index,i)
    if index==3:
        print("thisn is 3rd index")



marks2=[400,230,12,34,21]

for index, i in enumerate(marks2, start=1):#if want to print if condition before i use start value of index
    print(index,i)
    if index==3:
        print("thisn is 3rd index")




fruits=["bannaa","apple","lemon"]
for index, i in enumerate(fruits):
    print(f"{index+1}: {i}")
