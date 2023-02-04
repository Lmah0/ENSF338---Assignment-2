import sys
import json
from matplotlib import pyplot as plt
import timeit

sys.setrecursionlimit(20000) # This is used to maximize the amount of recursion, this helps prevent a stack overflow error if something such as infinite recursion was implemented.
def get_median(arr, low, high):
    mid = (high + low) // 2
    if arr[low] < arr[mid]:
        if arr[mid] < arr[high]:
            return mid # Return the middle index if the value is less than the upper index, and greater than the lower index. The arr[mid] is the median.
        elif arr[low] < arr[high]:
            return high  # Return the upper index. This means that arr[mid] >= arr[high], but arr[low] < arr[high]. Therefore arr[high] is the median.
        else:
            return low # This means that arr[low] < arr[mid], arr[mid] >= arr[high], and arr[low] >= arr[high]. Therefore arr[low] contains the median value.
    else:
        if arr[high] < arr[mid]:
            return mid # Return the middle index. This means arr[low] >= arr[mid] and arr[high] < arr[mid]. Therefore arr[mid] is the median value.
        elif arr[high] < arr[low]:
            return high # Return the upper index. This means arr[low] >= arr[mid], arr[high] >= arr[mid], and arr[high] < arr[low]. Therefore arr[high] is the median value.
        else:
            return low # Return the lower index. his means arr[low] >= arr[mid], arr[high] >= arr[mid], and arr[high] >= arr[low]. Therefore arr[low] is the median value.

def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high) # This is finding the pivot index, recursively, this is the index of the element that is in the correct posiiton
        func1(arr, low, pi-1) # This is calling on the bottom half of the array
        func1(arr, pi + 1, high) # This is calling on the top half of the array

def func1_optimized(arr, low, high):
    if low < high:
        pivot = get_median(arr, low, high) # This function compares the middle value, the first value, and last value. It returns the median value to make the best attempt at creating equal sub arrays to decrease the amount of recursive iterations.
        arr[low], arr[pivot] = arr[pivot], arr[low] # Swaps the pivot to the edge of the subarray for the quicksort
        pi = func2(arr, low, high) # This is finding the pivot index, recursively, this is the index of the element that is in the correct posiiton
        func1(arr, low, pi-1) # This is calling on the bottom half of the array
        func1(arr, pi + 1, high) # This is calling on the top half of the array

def func2(array, start, end): # This is called on with the sub-array
    p = array[start] # First element of the sub-array -  This is set as the pivot
    low = start + 1 # low is the index of the second element in the sub-array
    high = end # high is set to the same value of the last element in the array
    while True:
        while low <= high and array[high] >= p:
            high = high - 1 # Goes down from the upper half of the sub-array downwards, stops when the upper index is less than the lower index or if the element value of the upper index is less than the pivot 
        while low <= high and array[low] <= p:
            low = low + 1 # Goes from the lower half of the sub-array (excluding the pivot which is the lowest index) and goes downwards only stopping when the lower index is greater than the upper index, or if the value of the lower index is greater than the pivot
        if low <= high: # Swaps the elements that violate the boundaries of the pivot
            array[low], array[high] = array[high], array[low] # Swaps the elements in the low and high indices, this syntax makes it so that you don't have to use a temp variable
        else: # The lower index is greater than the high or upper index, exiting the loop
            break
    array[start], array[high] = array[high], array[start] # Swaps the pivot with the new index of high, the pivot is now placed in the correct position
    return high # returns the index of the element that is correctly sorted

def main():
    with open("Exercise2/ex2.json", "r") as file:
        data = json.load(file)
    
    entry_length = []
    entry_time = []

    entry_time_optimized = []

    for entry in data:
        end_length = len(entry)
        entry_length.append(end_length)
        
        elapsed_time = timeit.timeit(lambda : func1(entry, 0, end_length - 1), number = 1)
        entry_time.append(elapsed_time)

        elapsed_time = timeit.timeit(lambda : func1_optimized(entry, 0, end_length - 1), number = 1)
        entry_time_optimized.append(elapsed_time)

    for i in range(10):
        print("ENTRY LENGTH:", entry_length[i])
        print("Unoptimized time:", entry_time[i])
        print("Optimized time:", entry_time_optimized[i])
        print()
    
    plt.plot(entry_length, entry_time, label = "Unoptimized")
    plt.plot(entry_length, entry_time_optimized, label = "Optimized")
    plt.title("Quicksort Optimized: Length of Data vs. Time")
    plt.xlabel("Data Size")
    plt.ylabel("Time")
    plt.legend()
    plt.show()

    with open("sorted.json", "w") as file:
        json.dump(data, file)

if __name__ == '__main__':
    main()