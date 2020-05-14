import time

def analyze_func(func,*args) :
    """
    returns the time it takes to run the given function
    func -- a pointer to the function
    args -- any values to pass to the funciton
    returns a tuple with the value returned from the function call as well as the time taken to call it (in seconds)
    """
    tic = time.time()
    ret = func(*args)
    toc = time.time()
    seconds = toc-tic
    return ret, seconds
