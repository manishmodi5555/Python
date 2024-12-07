import threading
import time

from concurrent.futures import ThreadPoolExecutor # usefull to secedule multiple task


def fun(sec):
    print(f"sleeping for {sec} second")
    time.sleep(sec)
    return sec


# time1=time.perf_counter()
# #normal call
# fun(4)
# fun(3)
# fun(2)

#or


# same calling using therading
# t1=threading.Thread(target=fun, args=[5])
# t2=threading.Thread(target=fun, args=[3])
# t3=threading.Thread(target=fun, args=[2])


# t1.start() # run all the fun in background and and move to the end results
# t2.start()
# t3.start()

##or

# t1.join() # run all fun concurrenltly
# t2.join()
# t3.join()

# time2=time.perf_counter()
# print(time2-time1)




# example of theardpoolexecutor

def pool():
    with ThreadPoolExecutor() as exe:
        # future = exe.submit(fun,4)
        # future2 = exe.submit(fun, 3)
        # future3 = exe.submit(fun, 2)
        # print(future.result())
        # print(future2.result())
        # print(future3.result())


        #or


        # if have thousands of values we use list and use thread pool executor of multithreading like this
        l=[4,3,2]
        results=exe.map(fun,l)
        for result in results:
            print(result)




pool()
