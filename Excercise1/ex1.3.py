def fib2(n,cache = {}):
    if n == 0 or n == 1:
        return(n)
    else:
        if n in cache:
            return(cache[n])
        else:
            cache[n] = fib2(n-1) + fib2(n-2)
            return cache[n]
