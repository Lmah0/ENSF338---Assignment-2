import timeit
from matplotlib import pyplot as plt
def fib1(n):
    if n == 0 or n == 1:
        return(n)
    else:
        return(fib1(n-1) + fib1(n-2))
def fib2(n, cache = {}):
    if n == 0 or n == 1:
        return(n)
    else:
        if n in cache:
            return(cache[n])
        else:
            cache[n] = fib2(n-1) + fib2(n-2)
            return cache[n]

def main():
    optimizedTime = 0
    optimizedTimes = []
    nonOptimizedTime = 0
    nonOptimizedTimes = []
    for i in range(0,36):
        nonOptimizedTime += timeit.timeit(lambda: fib1(i), number = 1)
        nonOptimizedTimes.append(nonOptimizedTime)
        optimizedTime += timeit.timeit(lambda: fib2(i), number = 1)
        optimizedTimes.append(optimizedTime)

    print(f' the time taken by the non optimized code is {nonOptimizedTime} seconds')
    print(f' the time taken by the optimized code is {optimizedTime} seconds')
    plt.plot(nonOptimizedTimes, color = 'r')
    plt.title("Time taken by the non optimized code")
    plt.show()
    plt.plot(optimizedTimes, color = 'b')
    plt.title("Time taken by the optimized code")
    plt.show()
if __name__ == '__main__':
    main()