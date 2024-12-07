s={2,4,5,2,8}
print(s)

mk=set()
print(type(mk))

for i in s:
    print(i)


## sets methods
#union() and update()
s={1,2,3,4,5,10}
s2={2,7,9,8,10}
print(s.union(s2))

s.update(s2) # update the s combine with s2 avoid duplicate value
print(s)


#intersection and update_intersection
s4={2,3,4,5,6,10}
s5={2,3,9,7,10}
s3=s4.intersection(s5)
print(s3)

s4.intersection_update(s5)
print(s4)


#symmetri difference and difference and update
# value which is not in each other set
a1={2,3,45,9,7,6}
a2={2,6,10,11,22}
a3=a1.symmetric_difference(a2)
print(a3)

a4=a1.difference(a2)#show value for a1 only
print(a4)

a5=a1.symmetric_difference_update(a2)
print(a5)



b={1,2,3,4,5,6}
b2={11,23,43,1,2}

b3=b.isdisjoint(b2)
print(b3)

print(b2.issuperset(b))

b.add(11)
print(b)


##remove / discard remove give error discard not
b.remove(11)
print(b)
b.discard(80)


x=b.pop() # remove random value
print(b)
print(x)

# del b # clear whole set
# print(b)

b.clear() # clear values
print(b)

