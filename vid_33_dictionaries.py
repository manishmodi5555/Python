# a={'name':'manish modi',
#    101: "mukesh",
#    202:'anil',
#    'age': 20,
#    }
#
#
# print(a)
# print(a['name'])
# print(a.get("mk"))#if there is no value in varable it will not throw the error it will print none
#
# print(a.keys())# print all keys value
# print(a.values())# print all values of dictionaries
# print(a.items())
#
# for key in  a.keys():
#     print(f"there is key {key} and key values {a[key]}")
#
# for key,value in a.items():
#     print(f"yoo there is key {key} and key values {value}")
#


##methos of dict
ep1={101:22,202:33,205:23}
ep2={203:24,206:38,204:82}
ep3={101:22,202:33,205:23}
# update
ep1.update(ep2)
print(ep1)

ep3.clear()
print(ep3)

ep1.pop(101)
print(ep1)

ep1.popitem()#pop last item
print(ep1)

del ep3 # delete ep3
