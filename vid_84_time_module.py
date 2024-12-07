import time
# frist=time.time()# return time in seconds from 1january 1970 starting date
# print(frist)
#
# second=time.time() #return the time taken by the program to execute
# print(second)



# sleep() function

# print("hey")
# time.sleep(4)
# print("it will print after 4 sec")
#


#ctime() fun
# print(time.ctime(10000)) #skeep 10000 second from epoch time and print
# print(time.ctime())#print current time



#gmtime() and localtime()
# print(time.gmtime(10000))#return in struct form
# print(time.gmtime()) # current UTC time in struct form
#
# print(time.localtime()) #return system time
# sec1=time.localtime().tm_year #only return year
# print(sec1)
# sec=time.localtime()
# print("year",sec.tm_year)
# print("month",sec.tm_mon)


#strftime()
# print(time.strftime("%Y - %m - %d")) # return date in string form
# print(time.strftime("%H : %M : %S %p _ %Z")) # return time in string form


#strptime() return struct string into struct object reverse of strftime()
# todo=time.strftime("%H : %M : %S %p _ %Z")
# print(todo)
# print(time.strptime(todo,"%H : %M : %S %p _ %Z")) # string time into struct time object
#
#



#program : calculate the total execution time of your program using time modules
# start_time=time.time()
# for i in range(10000000):
#     va=i*i
# end_time=time.time()
# taken_time=end_time - start_time
# print(f"program execution time ( for loop) is: {taken_time}seconds")

#monotonic() fun gives 100 % correct time
# start_time=time.monotonic()
# for i in range(10000000):
#     va=i*i
# end_time=time.monotonic()
# taken_time=end_time - start_time
# print(f"program execution time ( for loop) is: {taken_time}seconds")

