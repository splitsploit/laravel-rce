import time, random
from functools import wraps

def fn_timer(function):
    @wraps(function)
    def function_timer(*args, **kwargs):
        func_n = str(function).split(' ')[1]
        #print func_n
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        print ("[{}]Total time running {} seconds".format(func_n,t1-t0))
    return function_timer


