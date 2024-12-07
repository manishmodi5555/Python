#we can change elements of list we cant change elements of tuple



# l=[1,2,8,3,"manish"]
# print(l)
# print(type(l))
# print(l[3])
# print(l[-2]) #nagative index
# print(l[len(l)-2])
# print(len(l)-2)
# print(len(l))

# print(l[:]) #print(l)
# print(l[1:]) # not print 1st elements
# print(l[1:3])
# print(l[1:4:2])


## list comprehension
# lst=[i for i in range(10)]
# print(lst)
#
# ## list comprehension
# lst=[i for i in range(10) if i%2==0]
# print(lst)
#
#
#
#
# if 7 in l:
#     print("yes")
# else:
#     print("no")
#
#
#
# m='im am manish '
# if "am" in m:
#     print("yoo")
# else:
#     print("noo")
#
# if "a" in "manish":
#     print("hell")




##list methods

l=[1,9,2,4,5,6,1,7]
print(l)
# l.append(0)
# print(l)

# l.reverse()
# print(l)

# l.sort()
# print(l)
# l.sort(reverse=True)# reverse the sort
# print(l)

# print(l.index(5))# give the index value of 1

print((l.count(1)))#how many times 1 comes in list


m=l.copy()
m[0]=0
print(m)
print(l)

l.insert(3, 10) # place 10 at index num 3
print(l)


j=[100,200,300]
k=l+j
print(k) # concate the l and j into k

l.extend(j)
print(l) # extend the j and add to l list



