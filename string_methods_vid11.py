
  ## string methods
# strin= 'im "manish" ' #we can use both "" or ''
# print(" hello",strin)
#
# strin2='''we use triple coma for
# multiple line
# as you can see'''# we can also use """ """
# print(strin2)
#
# print(strin[0])#it will print I first latter
# print(strin[5])
#
# for charactor in strin:
#     print(charactor) #it will print every single charactor in new line



#video 12 string slicing
# names= 'manish'
# print(names[0:5]) #it is not going to print 5th string it is include 0 but not 5
# print(names[0:2])
# print(names[1:5])
# print(names[:5])#it will automatically fill 0 to left side
#
# len1= len(names)
# print('the length of this string is ',len1)
# print(len(names)) #it will print the length of the string
#
# print(names[0:-4])#names[0:len(names)-4] output will be same 5-4 =1 name[0:1] it is include 0 and 1 and print
# print(names[-4:-1])



#video 13 string method
#Strings are immutable cant change
a="!!Mukesh!!! Mukesh rama!"
print(a.upper())
print(a.lower())
print(a.rstrip("!"))#it will remove the the element which is after the string not before
print(a.replace("Mukesh","rahul"))
print(a.split(" "))#make list of elements in the string

b='the maNish'
print(b.capitalize())# make first latter capital and also change others to small
print(b.center(50)) # place 50space before string also include string

print(a.count('Mukesh')) #how many times Mukesh comes in var a
print(a.count('e'))
print(a.endswith('!')) # output will be true or false
print(b.endswith('e',0,3))

c='mynameismanishimisabadboy132'
print(c.find('is'))# it will return index value of given string if not available then is will return -1
print(c.index('name'))#it is also return index value

print(c.isalnum())# it require A - Z a-z , numbers, not even space is allowed

f='alphabetsonly'
print(f.isalpha())# only aplphabets not spaces
print(f.islower())

g='allowed only printable char elements this is not allowed \n'
print(g.isprintable())#\n is not printable output will be false

a1='   '
print(a1.isspace())#only space

str='Im Mnaish Modi Im From Raj'
print(str.istitle())#every word first letter must be capital

print((str.swapcase()))#convert lower case into uper and lower into upper

str1='im manish modi'
print(str1.capitalize())# make first letter capital of first word only and also change others to small
print(str1.title()) # make first letter capital of every word in string


