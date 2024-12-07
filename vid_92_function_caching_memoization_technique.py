from functools import lru_cache
import time

@lru_cache(maxsize=None)
def fx(n):
    time.sleep(2)
    return n*5

print(fx(2))
print("done for 2")
print(fx(4))
print("done for 4")
print(fx(10))
print("done for 10")

# this is print immediatly becouse values are stored in cache for same number results
print(fx(2))
print("done for 2")
print(fx(4))
print("done for 4")
print(fx(10))
print("done for 10")

print(fx(6))
print("done for 6 it take 2 sec again unknown values ")
