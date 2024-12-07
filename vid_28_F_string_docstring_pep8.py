##using f string u can use same varbale for printing the value multiple times
#you have to declare f at starting and we use {} for varible declare
name="manish"
place="ahemdabad"
print(f"hey my name is {name} and im from {place}")
print(f" his name is  {name} and he is  from {place}")


price = 49.2029
txt=f"for only {price} doller"
print(txt)


print(f"{2*5}")


##if you want to print brekets you use duble brekets
print(f"hey my name is {{name}} and im from {place}")



###docstring

def add(a,b):
    '''
    this is doc string
    '''
    print(a+b)

add(5,10)
print(add.__doc__)



##pep 8
# open terminal write python and
# write import this